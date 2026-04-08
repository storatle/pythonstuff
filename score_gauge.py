import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

COLORS = {
    'dark-blue':  '#00639C',
    'blue':       '#0097E9',
    'light-blue': '#93CCFF',
    'yellow':     '#FFC107',
    'red':        '#F44336',
}

def draw_score_gauge(score=83, max_score=100, gap_degrees=40, label='Score', color='#0097E9', bg_color='white'):
    fig, ax = plt.subplots(figsize=(5, 5))
    ax.set_aspect('equal')
    ax.axis('off')

    # --- Parameters ---
    center = (0.5, 0.5)
    radius = 0.38
    linewidth = 18

    cw_start = 90 - gap_degrees / 2   # right edge of gap (clockwise start, near top)

    # Background arc (grey, full circle)
    theta_bg = np.linspace(0, 2 * np.pi, 500)
    x_bg = center[0] + radius * np.cos(theta_bg)
    y_bg = center[1] + radius * np.sin(theta_bg)
    ax.plot(x_bg, y_bg, color='#e0e0e0', linewidth=linewidth,
            solid_capstyle='round', transform=ax.transAxes, zorder=1)

    # Foreground arc (blue, proportional to score, clockwise)
    fraction = score / max_score
    arc_span = (360 - gap_degrees) * fraction
    cw_end = cw_start - arc_span
    theta_fg = np.linspace(np.radians(cw_start), np.radians(cw_end), 500)
    x_fg = center[0] + radius * np.cos(theta_fg)
    y_fg = center[1] + radius * np.sin(theta_fg)
    ax.plot(x_fg, y_fg, color=color, linewidth=linewidth,
            solid_capstyle='round', transform=ax.transAxes, zorder=2)

    # --- Bar chart icon (3 bars) ---
    bar_x = [0.44, 0.50, 0.56]
    bar_heights = [0.055, 0.085, 0.055]
    bar_bottoms = [0.575, 0.575, 0.575]
    bar_width = 0.028
    for bx, bh, bb in zip(bar_x, bar_heights, bar_bottoms):
        rect = mpatches.FancyBboxPatch(
            (bx - bar_width / 2, bb), bar_width, bh,
            boxstyle="round,pad=0.005",
            facecolor=color, edgecolor='none',
            transform=ax.transAxes, zorder=3
        )
        ax.add_patch(rect)

    # --- Score number ---
    ax.text(0.5, 0.46, str(score),
            ha='center', va='center',
            fontsize=32, fontweight='bold', color='#111111',
            transform=ax.transAxes, zorder=4)

    # --- "Score" label ---
    ax.text(0.5, 0.36, label,
            ha='center', va='center',
            fontsize=14, color='#444444',
            transform=ax.transAxes, zorder=4)

    fig.patch.set_facecolor(bg_color)
    plt.tight_layout()
    plt.savefig('score_gauge_output.png', dpi=150, bbox_inches='tight',
                facecolor=bg_color)
    print("Saved as score_gauge_output.png")

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--score', type=int, default=83)
    parser.add_argument('--max-score', type=int, default=100)
    parser.add_argument('--gap', type=float, default=40, help='Gap at the bottom in degrees')
    parser.add_argument('--label', type=str, default='Score')
    parser.add_argument('--color', type=str, default='blue', choices=COLORS.keys())
    parser.add_argument('--bg-color', type=str, default='white', help='Background color (any CSS color or hex)')
    args = parser.parse_args()
    draw_score_gauge(score=args.score, max_score=args.max_score, gap_degrees=args.gap, label=args.label, color=COLORS[args.color], bg_color=args.bg_color)
