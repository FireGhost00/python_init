serie = 'N-02'

match serie:
    case 'N-01':
        print("Samsung")
    case 'N-02':
        print("Apple")
    case 'N-03':
        print("Huawei")
    case _:
        print("Marca no reconocida")