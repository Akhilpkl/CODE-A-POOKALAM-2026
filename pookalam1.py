import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Ellipse, Polygon

np.random.seed(42)

FIG_SIZE = 14
DPI = 400

YELLOW = "#F7C928"
GOLD = "#F4A51C"
MARIGOLD = "#F58216"
ORANGE = "#ED6415"
RED = "#B82D24"
CRIMSON = "#9D1830"
PINK = "#E64A91"
HOT_PINK = "#C72B83"
PURPLE = "#65145F"
VIOLET = "#7B267A"
WHITE = "#FFF6DC"
CREAM = "#F3E5C2"
GREEN = "#2E793C"
DARK_GREEN = "#174B2A"
LIGHT_GREEN = "#56A64B"
LIME = "#8BBE39"

fig, ax = plt.subplots(figsize=(FIG_SIZE, FIG_SIZE))
ax.set_aspect("equal")
ax.set_xlim(-11, 11)
ax.set_ylim(-12, 11)
ax.axis("off")

fig.patch.set_facecolor("#202020")
ax.set_facecolor("#202020")


def polar(r, angle):
    return r * np.cos(angle), r * np.sin(angle)


def circle(r, color, z=1, edge=None, lw=0):
    ax.add_patch(
        Circle(
            (0, 0), r,
            facecolor=color,
            edgecolor=edge if edge else "none",
            linewidth=lw,
            zorder=z
        )
    )


def dot(x, y, r, color, z=10):
    ax.add_patch(
        Circle(
            (x, y), r,
            facecolor=color,
            edgecolor="none",
            zorder=z
        )
    )


def ellipse(x, y, w, h, angle, color, z=10):
    ax.add_patch(
        Ellipse(
            (x, y),
            w,
            h,
            angle=np.degrees(angle),
            facecolor=color,
            edgecolor="none",
            zorder=z
        )
    )


def pointed_petal(
    cx, cy,
    direction,
    length,
    width,
    color,
    z=20,
    inner_color=None
):
    ux = np.cos(direction)
    uy = np.sin(direction)

    vx = -uy
    vy = ux

    base = (cx, cy)

    left = (
        cx + width * vx,
        cy + width * vy
    )

    right = (
        cx - width * vx,
        cy - width * vy
    )

    shoulder1 = (
        cx + length * 0.55 * ux + width * 0.70 * vx,
        cy + length * 0.55 * uy + width * 0.70 * vy
    )

    shoulder2 = (
        cx + length * 0.55 * ux - width * 0.70 * vx,
        cy + length * 0.55 * uy - width * 0.70 * vy
    )

    tip = (
        cx + length * ux,
        cy + length * uy
    )

    ax.add_patch(
        Polygon(
            [base, left, shoulder1, tip, shoulder2, right],
            closed=True,
            facecolor=color,
            edgecolor="none",
            zorder=z
        )
    )

    if inner_color:
        inner_len = length * 0.67
        inner_w = width * 0.45

        ix = cx + length * 0.18 * ux
        iy = cy + length * 0.18 * uy

        pointed_petal(
            ix, iy,
            direction,
            inner_len,
            inner_w,
            inner_color,
            z=z + 1
        )


def round_petal(cx, cy, direction, length, width, color, z=20):
    ux = np.cos(direction)
    uy = np.sin(direction)

    px = cx + length * 0.42 * ux
    py = cy + length * 0.42 * uy

    ellipse(
        px, py,
        length,
        width,
        direction,
        color,
        z
    )


def small_flower(
    cx, cy,
    radius=.22,
    petals=8,
    petal_color=WHITE,
    center=GOLD,
    z=30
):
    for i in range(petals):
        a = 2*np.pi*i/petals
        round_petal(
            cx, cy, a,
            radius * 1.45,
            radius * .48,
            petal_color,
            z
        )

    dot(cx, cy, radius*.28, center, z+2)


def marigold(
    cx, cy,
    radius=.28,
    petals=12,
    color=MARIGOLD,
    center=ORANGE,
    z=30
):
    for i in range(petals):
        a = 2*np.pi*i/petals
        round_petal(
            cx, cy, a,
            radius * 1.20,
            radius * .45,
            color,
            z
        )

    dot(cx, cy, radius*.30, center, z+2)


def lotus_medallion(
    cx, cy,
    size=1.0,
    outer=PINK,
    middle=HOT_PINK,
    inner=WHITE,
    z=40
):
    for i in range(6):
        a = 2*np.pi*i/6
        x, y = polar(size*.42, a)
        x += cx
        y += cy
        pointed_petal(
            x, y, a,
            size*.80, size*.23,
            DARK_GREEN,
            z=z
        )

    for i in range(8):
        a = 2*np.pi*i/8
        pointed_petal(
            cx, cy, a,
            size*1.05,
            size*.33,
            outer,
            z=z+2
        )

    for i in range(8):
        a = 2*np.pi*i/8 + np.pi/8
        pointed_petal(
            cx, cy, a,
            size*.78,
            size*.26,
            middle,
            z=z+4
        )

    for i in range(6):
        a = 2*np.pi*i/6
        pointed_petal(
            cx, cy, a,
            size*.53,
            size*.18,
            inner,
            z=z+6
        )

    dot(cx, cy, size*.12, GOLD, z+8)


def leaf(cx, cy, direction, length, width, color=DARK_GREEN, z=20):
    ux = np.cos(direction)
    uy = np.sin(direction)

    vx = -uy
    vy = ux

    base = (cx, cy)

    tip = (
        cx + length*ux,
        cy + length*uy
    )

    p1 = (
        cx + length*.48*ux + width*vx,
        cy + length*.48*uy + width*vy
    )

    p2 = (
        cx + length*.48*ux - width*vx,
        cy + length*.48*uy - width*vy
    )

    ax.add_patch(
        Polygon(
            [base, p1, tip, p2],
            closed=True,
            facecolor=color,
            edgecolor="none",
            zorder=z
        )
    )


def leaf_ring(radius, count, length, width, colors, z=20):
    for i in range(count):
        a = 2*np.pi*i/count
        x, y = polar(radius, a)
        leaf(
            x, y, a,
            length,
            width,
            colors[i % len(colors)],
            z
        )


def flower_ring(
    radius,
    count,
    flower_radius,
    flower_type="small",
    colors=None,
    offset=0,
    z=30
):
    if colors is None:
        colors = [WHITE]

    for i in range(count):
        a = offset + 2*np.pi*i/count
        x, y = polar(radius, a)

        if flower_type == "marigold":
            marigold(
                x, y,
                flower_radius,
                11,
                colors[i % len(colors)],
                ORANGE,
                z
            )
        else:
            small_flower(
                x, y,
                flower_radius,
                8,
                colors[i % len(colors)],
                GOLD,
                z
            )


def bead_ring(radius, count, bead_radius, colors, z=50):
    for i in range(count):
        a = 2*np.pi*i/count
        x, y = polar(radius, a)

        dot(
            x, y,
            bead_radius,
            colors[i % len(colors)],
            z
        )


def scallop_ring(radius, count, size, color, z=20):
    for i in range(count):
        a = 2*np.pi*i/count
        x, y = polar(radius, a)
        dot(x, y, size, color, z)


circle(10.25, DARK_GREEN, 1)

leaf_ring(
    9.82, 84,
    .62, .18,
    [DARK_GREEN, GREEN, DARK_GREEN],
    z=5
)

circle(9.58, CREAM, 6)

bead_ring(
    9.43, 84, .105,
    [GOLD, YELLOW, ORANGE],
    z=12
)

circle(9.23, WHITE, 10)

flower_ring(
    8.98, 72, .18,
    "small",
    [WHITE, CREAM],
    z=18
)

circle(8.60, PURPLE, 20)

scallop_ring(
    8.48, 48, .22,
    VIOLET,
    z=23
)

circle(8.08, ORANGE, 25)

for i in range(32):
    a = 2*np.pi*i/32
    x, y = polar(7.75, a)

    for j in [-1, 0, 1]:
        pointed_petal(
            x, y,
            a + j*.16,
            .90,
            .28,
            MARIGOLD if (i+j) % 2 else GOLD,
            z=30
        )

for i in range(24):
    a = 2*np.pi*i/24 + np.pi/24
    x, y = polar(7.05, a)

    lotus_medallion(
        x, y,
        .67,
        PINK,
        HOT_PINK,
        WHITE,
        z=36
    )

for i in range(24):
    a = 2*np.pi*i/24
    x, y = polar(6.55, a)
    leaf(x, y, a, .72, .20, DARK_GREEN, z=40)

circle(6.20, DARK_GREEN, 43)

flower_ring(
    5.88, 32, .25,
    "small",
    [WHITE],
    offset=np.pi/32,
    z=48
)

bead_ring(
    5.55, 64, .075,
    [GOLD, YELLOW],
    z=53
)

circle(5.39, PURPLE, 55)

circle(5.16, GOLD, 57)

circle(4.93, RED, 60)

for i in range(24):
    a = 2*np.pi*i/24

    x, y = polar(4.25, a)

    pointed_petal(
        x, y,
        a,
        1.02,
        .36,
        ORANGE if i % 2 else MARIGOLD,
        z=65
    )

for i in range(24):
    a = 2*np.pi*i/24 + np.pi/24
    x, y = polar(3.88, a)

    pointed_petal(
        x, y,
        a,
        .90,
        .27,
        YELLOW,
        z=68
    )

circle(3.66, CRIMSON, 72)

for i in range(8):
    a = 2*np.pi*i/8

    pointed_petal(
        0, 0,
        a,
        3.05,
        .86,
        WHITE,
        z=78
    )

    pointed_petal(
        0, 0,
        a,
        2.63,
        .68,
        PINK,
        z=80
    )

    pointed_petal(
        0, 0,
        a,
        2.16,
        .52,
        PURPLE,
        z=82
    )

    pointed_petal(
        0, 0,
        a,
        1.68,
        .28,
        HOT_PINK,
        z=84
    )

circle(2.02, GREEN, 90)

bead_ring(
    1.92, 32, .075,
    [WHITE, GOLD],
    z=94
)

for i in range(12):
    a = 2*np.pi*i/12

    x, y = polar(1.32, a)

    pointed_petal(
        x, y,
        a,
        .90,
        .23,
        LIME,
        z=98
    )

    x2, y2 = polar(1.15, a + np.pi/12)

    ellipse(
        x2, y2,
        .64, .17,
        a,
        YELLOW,
        z=100
    )

bead_ring(
    1.55, 16, .08,
    [WHITE],
    z=105
)

circle(1.12, PURPLE, 108)

for i in range(8):
    a = 2*np.pi*i/8
    pointed_petal(
        0, 0,
        a,
        1.05,
        .30,
        WHITE,
        z=112
    )

for i in range(8):
    a = 2*np.pi*i/8 + np.pi/8
    pointed_petal(
        0, 0,
        a,
        .78,
        .23,
        YELLOW,
        z=115
    )

for i in range(8):
    a = 2*np.pi*i/8
    round_petal(
        0, 0,
        a,
        .55,
        .18,
        ORANGE,
        z=118
    )

dot(0, 0, .22, RED, 122)
dot(0, 0, .10, GOLD, 124)

for i in range(16):
    a = 2*np.pi*i/16 + np.pi/16
    x, y = polar(3.02, a)

    small_flower(
        x, y,
        .19,
        7,
        WHITE,
        ORANGE,
        z=130
    )

for i in range(24):
    a = 2*np.pi*i/24
    x, y = polar(4.62, a)

    marigold(
        x, y,
        .13,
        9,
        GOLD,
        ORANGE,
        z=135
    )


def diya(cx, cy, rotation=0):
    for delta in [-.55, -.18, .18, .55]:
        leaf(
            cx, cy,
            rotation + delta,
            .72,
            .17,
            DARK_GREEN,
            z=140
        )

    ellipse(
        cx, cy,
        .90, .36,
        rotation,
        "#D39A19",
        z=145
    )

    ellipse(
        cx, cy+.02,
        .62, .17,
        rotation,
        "#F5C63A",
        z=147
    )

    ux = np.cos(rotation)
    uy = np.sin(rotation)

    flame_x = cx + .03*ux
    flame_y = cy + .03*uy

    flame = [
        (flame_x, flame_y+.15),
        (flame_x-.12, flame_y+.48),
        (flame_x, flame_y+.82),
        (flame_x+.12, flame_y+.48)
    ]

    ax.add_patch(
        Polygon(
            flame,
            closed=True,
            facecolor=GOLD,
            edgecolor="none",
            zorder=150
        )
    )

    inner = [
        (flame_x, flame_y+.22),
        (flame_x-.055, flame_y+.46),
        (flame_x, flame_y+.65),
        (flame_x+.055, flame_y+.46)
    ]

    ax.add_patch(
        Polygon(
            inner,
            closed=True,
            facecolor="#FFF2A6",
            edgecolor="none",
            zorder=151
        )
    )


for a in [0, np.pi/2, np.pi, 3*np.pi/2]:
    x, y = polar(8.28, a)
    diya(x, y, a)

for a in [0, np.pi/2, np.pi, 3*np.pi/2]:
    cx, cy = polar(8.28, a)

    pointed_petal(
        cx, cy,
        a,
        .92,
        .34,
        CRIMSON,
        z=138
    )

    pointed_petal(
        cx, cy,
        a,
        .67,
        .23,
        GOLD,
        z=139
    )

for a in [0, np.pi/2, np.pi, 3*np.pi/2]:
    x, y = polar(8.28, a)
    diya(x, y, a)

for radius, count, size in [
    (9.62, 96, .045),
    (8.72, 96, .038),
    (6.36, 72, .045),
    (5.25, 72, .038),
    (4.78, 64, .035)
]:
    for i in range(count):
        a = 2*np.pi*i/count
        x, y = polar(radius, a)
        dot(
            x, y, size,
            YELLOW if i % 2 else WHITE,
            z=160
        )

for i in range(56):
    a = 2*np.pi*i/56

    x, y = polar(10.0, a)

    pointed_petal(
        x, y,
        a,
        .53,
        .16,
        YELLOW,
        z=165
    )

for i in range(72):
    a = 2*np.pi*i/72
    x, y = polar(9.76, a)
    dot(x, y, .065, ORANGE, z=170)

for a in [np.pi/4, 3*np.pi/4, 5*np.pi/4, 7*np.pi/4]:
    cx, cy = polar(2.05, a)

    for j in range(5):
        aa = a + (j-2)*.22
        pointed_petal(
            cx, cy,
            aa,
            .40,
            .14,
            YELLOW,
            z=176
        )

    dot(cx, cy, .08, ORANGE, z=178)

ax.text(
    0, -11.15,
    "HAPPY ONAM",
    ha="center",
    va="center",
    fontsize=22,
    fontweight="bold",
    color=WHITE,
    zorder=200
)

plt.tight_layout(pad=0)

plt.savefig(
    "ai_competition_pookalam.png",
    dpi=DPI,
    bbox_inches="tight",
    facecolor=fig.get_facecolor()
)

plt.show()