import itertools

# Faylların adlarını təyin edirik
input_file = "input2.txt"
output_file = "output.txt"

# Subdomen və domen siyahılarını oxumaq
def read_input_file(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()
        # Birinci sətirdə prefikslər, qalan sətirlərdə domenlər
        prefixes = lines[0].strip().split(",")
        domains = [line.strip() for line in lines[1:] if line.strip()]
        return prefixes, domains

# Kombinasiyaları yaradıb fayla yazmaq
def generate_subdomains_to_file(prefixes, domains, output_path):
    with open(output_path, "w") as file:
        print("Yaradılmış subdomen kombinasiyaları:\n")
        for prefix, domain in itertools.product(prefixes, domains):
            subdomain = f"{prefix}.{domain}"
            print(subdomain)  # Ekrana çap edir
            file.write(subdomain + "\n")  # Fayla yazır

# Əsas funksiya
def main():
    input_path = input_file
    output_path = output_file

    # input.txt faylından prefikslər və domenlər oxunur
    prefixes, domains = read_input_file(input_path)

    # Kombinasiyalar yaradılır və output.txt faylına yazılır
    generate_subdomains_to_file(prefixes, domains, output_path)

    print(f"\n✅ Nəticələr '{output_path}' faylında saxlanıldı.")

if __name__ == "__main__":
    main()
