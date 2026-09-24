import gradio as gr
from ndvi_calculator import compute_ndvi, generate_color_bar

def handle_calculation(red, nir):
    if red is None or nir is None:
        return "", "", None
    try:
        result = compute_ndvi(red, nir)
        ndvi_val = result["ndvi"]
        classification = result["classification"]
        # Generate color bar figure
        fig = generate_color_bar(ndvi_val)
        # Determine badge color based on NDVI
        if ndvi_val < 0:
            badge_color = "#ff4444"  # red
        elif ndvi_val < 0.2:
            badge_color = "#ffcc00"  # yellow
        else:
            badge_color = "#44aa44"  # green
        badge_html = f'<div style="background:{badge_color}; color:white; padding:8px 16px; border-radius:8px; font-size:1.2em; font-weight:bold; display:inline-block;">NDVI = {ndvi_val:.3f}</div>'
        return badge_html, classification, fig
    except ValueError as e:
        return f"<div style='color:red;'>Error: {e}</div>", "", None

with gr.Blocks(title="NDVI Calculator") as demo:
    gr.Markdown("# NDVI Calculator")
    gr.Markdown("Enter Red and NIR reflectance values (0.0–1.0) to compute the Normalized Difference Vegetation Index.")
    with gr.Row():
        red_input = gr.Number(label="Red Reflectance (0.0–1.0)", minimum=0.0, maximum=1.0, step=0.01, value=0.2)
        nir_input = gr.Number(label="NIR Reflectance (0.0–1.0)", minimum=0.0, maximum=1.0, step=0.01, value=0.5)
    calc_btn = gr.Button("Calculate")
    ndvi_output = gr.HTML(label="NDVI Value")
    class_output = gr.Textbox(label="Classification", interactive=False)
    colorbar_output = gr.Plot(label="Color Bar")
    calc_btn.click(
        fn=handle_calculation,
        inputs=[red_input, nir_input],
        outputs=[ndvi_output, class_output, colorbar_output]
    )

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)
