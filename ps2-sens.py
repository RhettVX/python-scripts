class PS2Sensitivity:

    def __init__(self, dpi: int):
        self.dpi = dpi

    def to_float(self, cm: float, zoom: float = None) -> float:
        if zoom:
            return round(-0.3 + 11.7581 / (cm * self.dpi / (1.6* zoom)) ** (1 / 3), 6)
        return round(-0.3 + 11.7581 / (cm * self.dpi) ** (1 / 3), 6)

    def to_ini(self, cm: float, zoom: float = None) -> str:
        key = ''
        if zoom:
            if zoom < 3.4:
                key = 'ADSMouseSensitivity'
            elif zoom >= 3.4:
                key = 'ScopedMouseSensitivity'
        else:
            key = 'MouseSensitivity'

        return f'{key}={self.to_float(cm, zoom)}'


if __name__ == '__main__':
    senses = []

    my_sens = PS2Sensitivity(400)
    base_cm = 35

    senses.append(f'; dpi: {my_sens.dpi}, cm360: {base_cm}/{base_cm*2}/{base_cm*4}')
    senses.append(my_sens.to_ini(base_cm))
    senses.append(my_sens.to_ini(base_cm*2, 1.35))
    senses.append(my_sens.to_ini(base_cm*4, 4))
    #senses.append(f'VehicleGunnerMouseSensitivity={my_sens.to_float(base_cm)}')
    #senses.append(f'VehicleMouseSensitivity={my_sens.to_float(base_cm, 1+1/3)}')

    print('\n'.join(senses))


