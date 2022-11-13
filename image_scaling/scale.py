def negative_image() -> None:
    with open("dog.pgm") as file_in:
        lines = []
        for line in file_in:
            lines.append(line)
        file_in.close()

    with open("scale_transformed_dog.pgm", "w") as file_out:
        file_out.close()

    with open("scale_transformed_dog.pgm", "a") as file_out:
        pixels = []
        new_image = []

        for line in lines[4:]:
            pixels.append(int(line))

        r_max = max(pixels)
        r_min = min(pixels)
        k = 255

        for i in range(4):
            new_image.append(lines[i])
        for pixel in pixels:
            new_image.append(str(round(k*(pixel - r_min)/(r_max - r_min))) + "\n")

        for line in new_image:
            file_out.writelines(line)

        file_out.close()

def main() -> None:
    negative_image()

if __name__ == "__main__":
    main()