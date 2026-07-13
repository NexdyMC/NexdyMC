def generate_stats():
    svg = """
    <svg>
        ...
    </svg>
    """

    with open("assets/stats/stats.svg", "w") as f:
        f.write(svg)