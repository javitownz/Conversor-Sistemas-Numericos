def binary_to_decimal(binary_str):
    if '.' in binary_str:
        whole, frac = binary_str.split('.')
        whole_decimal = int(whole, 2)
        frac_decimal = sum(int(bit) * (2 ** -(i + 1)) for i, bit in enumerate(frac))
        return whole_decimal + frac_decimal
    else:
        return int(binary_str, 2)


def decimal_to_binary(decimal_num):
    whole, frac = str(decimal_num).split(".")
    whole = int(whole)
    frac = float(f"0.{frac}")

    # Convierte todo
    whole_bin = bin(whole).replace("0b", "")

    # Convierte la parte fraccional
    frac_bin = ""
    while frac and len(frac_bin) < 10:
        frac *= 2
        if frac >= 1:
            frac_bin += "1"
            frac -= 1
        else:
            frac_bin += "0"

    return f"{whole_bin}.{frac_bin}" if frac_bin else whole_bin


def decimal_to_octal(decimal_num):
    whole = int(decimal_num)
    frac = decimal_num - whole
    octal_whole = oct(whole).replace("0o", "")

    # Conversion fraccional
    octal_frac = ""
    while frac and len(octal_frac) < 10:
        frac *= 8
        digit = int(frac)
        octal_frac += str(digit)
        frac -= digit

    return f"{octal_whole}.{octal_frac}" if octal_frac else octal_whole


def decimal_to_hexadecimal(decimal_num):
    whole = int(decimal_num)
    frac = decimal_num - whole
    hex_whole = hex(whole).replace("0x", "")

    # Conversion fraccional
    hex_frac = ""
    while frac and len(hex_frac) < 10:
        frac *= 16
        digit = int(frac)
        hex_frac += hex(digit).replace("0x", "")
        frac -= digit

    return f"{hex_whole}.{hex_frac}" if hex_frac else hex_whole


def octal_to_decimal(octal_str):
    if '.' in octal_str:
        whole, frac = octal_str.split('.')
        whole_decimal = int(whole, 8)
        frac_decimal = sum(int(bit) * (8 ** -(i + 1)) for i, bit in enumerate(frac))
        return whole_decimal + frac_decimal
    else:
        return int(octal_str, 8)


def hex_to_decimal(hex_str):
    if '.' in hex_str:
        whole, frac = hex_str.split('.')
        whole_decimal = int(whole, 16)
        frac_decimal = sum(int(char, 16) * (16 ** -(i + 1)) for i, char in enumerate(frac))
        return whole_decimal + frac_decimal
    else:
        return int(hex_str, 16)


# Menu
def main():
    while True:
        print("\nOpciones de conversión:")
        print("1. Binario a Decimal, Octal y Hexadecimal")
        print("2. Decimal a Binario, Octal y Hexadecimal")
        print("3. Octal a Decimal, Binario y Hexadecimal")
        print("4. Hexadecimal a Decimal, Binario y Octal")
        print("5. Salir")

        option = input("\nSelecciona una opción: ")

        if option == "1":
            binary = input("Introduce un número binario: ")
            decimal = binary_to_decimal(binary)
            print(f"Decimal: {decimal}")
            print(f"Octal: {decimal_to_octal(decimal)}")
            print(f"Hexadecimal: {decimal_to_hexadecimal(decimal)}")

        elif option == "2":
            decimal = float(input("Introduce un número decimal: "))
            print(f"Binario: {decimal_to_binary(decimal)}")
            print(f"Octal: {decimal_to_octal(decimal)}")
            print(f"Hexadecimal: {decimal_to_hexadecimal(decimal)}")

        elif option == "3":
            octal = input("Introduce un número octal: ")
            decimal = octal_to_decimal(octal)
            print(f"Decimal: {decimal}")
            print(f"Binario: {decimal_to_binary(decimal)}")
            print(f"Hexadecimal: {decimal_to_hexadecimal(decimal)}")

        elif option == "4":
            hex_num = input("Introduce un número hexadecimal: ")
            decimal = hex_to_decimal(hex_num)
            print(f"Decimal: {decimal}")
            print(f"Binario: {decimal_to_binary(decimal)}")
            print(f"Octal: {decimal_to_octal(decimal)}")

        elif option == "5":
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")



if __name__ == "__main__":
    main()
