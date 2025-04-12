from MDOF_to_SDOF.MDOF import MDOF


if __name__ == "__main__":
    # frame = MDOF(period=2.2152, mass=[100, 200, 300], height=[0, 10, 20], mode=[0.0190431, 0.0365541, 0.0481835], gravity=[3, 0, 0])
    frame = MDOF(
        period=1.161,
        mass=[281.596, 280.476, 280.476, 232.731],
        height=[4300, 8300, 12300, 16300],
        mode=[4300, 8300, 12300, 16300],
        gravity=[0, 0, 0]
    )
    print(frame.SDOF_initial_stiffness)
    print(frame.SDOF_mass)
