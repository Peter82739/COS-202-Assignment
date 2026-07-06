print("MATHEMATICAL CALCULATOR")

while True:

    print("\n+, -, *, /, \\, ^, %, C, OFF")

    choice = input("Enter Operation: ").upper()

    match choice:

        case "OFF":
            print("Calculator Closed")
            break

        case "C":
            print("Screen Cleared")

        case "+" | "-" | "*" | "/" | "\\" | "^" | "%":

            num1 = float(input("Enter First Number: "))
            num2 = float(input("Enter Second Number: "))

            match choice:

                case "+":
                    answer = num1 + num2

                case "-":
                    answer = num1 - num2

                case "*":
                    answer = num1 * num2

                case "/":
                    if num2 == 0:
                        print("Cannot Divide by Zero")
                        continue
                    answer = num1 / num2

                case "\\":
                    if num2 == 0:
                        print("Cannot Divide by Zero")
                        continue
                    answer = num1 // num2

                case "^":
                    answer = num1 ** num2

                case "%":
                    if num2 == 0:
                        print("Cannot Divide by Zero")
                        continue
                    answer = num1 % num2

            print("Answer =", answer)

        case _:
            print("Invalid Choice")