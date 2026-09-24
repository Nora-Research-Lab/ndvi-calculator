import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

plt.switch_backend('agg')  # Non-interactive backend for headless environment

def compute_ndvi(red: float, nir: float) -> dict:
    """
    Compute NDVI from red and NIR reflectance values (0.0–1.0).
    Returns dict with 'ndvi' (float) and 'classification' (str).
    Raises ValueError if inputs are out of range.
    """
    if not (0.0 <= red <= 1.0):
        raise ValueError("Red reflectance must be between 0.0 and 1.0")
    if not (0.0 <= nir <= 1.0):
        raise ValueError("NIR reflectance must be between 0.0 and 1.0")
    denominator = nir + red
    if denominator == 0.0:
        ndvi = 0.0
    else:
        ndvi = (nir - red) / denominator
    # Clamp to [-1, 1] due to possible floating point errors
    ndvi = max(-1.0, min(1.0, ndvi))
    # Determine classification
    if ndvi < 0:
        classification = "Water / Non-vegetated"
    elif ndvi < 0.2:
        classification = "Bare Soil / Sparse Vegetation"
    elif ndvi < 0.4:
        classification = "Moderate Vegetation"
    elif ndvi < 0.6:
        classification = "Dense Vegetation"
    else:
        classification = "Very Dense Vegetation"
    return {"ndvi": ndvi, "classification": classification}

def generate_color_bar(ndvi: float):
    """
    Generate a matplotlib figure showing a horizontal color bar
    from red (-1) through yellow/green to dark green (+1) with a marker.
    """
    # Create custom colormap: red -> yellow -> green -> dark green
    # Stops: 0.0: red, 0.33: yellow, 0.66: green, 1.0: dark green
    cdict = {
        'red':   [(0.0, 0.8, 0.8),
                  (0.33, 1.0, 1.0),
                  (0.66, 0.0, 0.0),
                  (1.0, 0.0, 0.0)],
        'green': [(0.0, 0.0, 0.0),
                  (0.33, 1.0, 1.0),
                  (0.66, 0.5, 0.5),
                  (1.0, 0.3, 0.3)],
        'blue':  [(0.0, 0.0, 0.0),
                  (0.33, 0.0, 0.0),
                  (0.66, 0.0, 0.0),
                  (1.0, 0.0, 0.0)]
    }
    cmap = mcolors.LinearSegmentedColormap('ndvi_cmap', cdict, 256)
    norm = mcolors.Normalize(vmin=-1, vmax=1)
    fig, ax = plt.subplots(figsize=(6, 0.8))
    # Create gradient image
    gradient = np.linspace(-1, 1, 256).reshape(1, -1)
    ax.imshow(gradient, aspect='auto', cmap=cmap, norm=norm,
              extent=[-1, 1, 0, 1])
    # Add marker
    ax.axvline(x=ndvi, ymin=0, ymax=1, color='black', linewidth=2)
    # Formatting
    ax.set_xlim(-1, 1)
    ax.set_ylim(0, 1)
    ax.set_yticks([])
    ax.set_xticks([-1, -0.5, 0, 0.5, 1])
    ax.set_xlabel('NDVI')
    plt.tight_layout()
    return fig
