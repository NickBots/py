import matplotlib.pyplot as plt
from pyplutchik import plutchik

import base64, io


def plot(z_scores):
    fig=plt.figure(figsize=(7,7))
    ax1 = fig.add_subplot(1,1,1)
    plutchik(z_scores, ax=ax1)
    bytes_array = io.BytesIO()
    fig.savefig(bytes_array, format='svg')
    bytes_array.seek(0)
    svgData = base64.b64encode(bytes_array.read())
    return str(svgData)[2:-1]