#!/usr/bin/env python3
# Created By: Emmanuella Taiwo
# created on 14th november, 2026
# This program gets input user that determine
# the colour code either red, green or blue for the output


def main():
    # Get the colour code limits from the user.
    try:
        red_input = int(input("Enter a number for red: "))
        green_input = int(input("Enter a number for green: "))
        blue_input = int(input("Enter a number for blue: "))

        # Print every RGB combination from zero through each entered limit.
        for red in range(red_input + 1):
            for green in range(green_input + 1):
                for blue in range(blue_input + 1):
                    print(f"{red},{green},{blue}")
    except ValueError:
        print("Please enter whole numbers.")


if __name__ == "__main__":
    main()
