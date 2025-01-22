from src.detector import detect_dns_poisoning
from src.report_generator import generate_pdf_report

def main():
    print("Starting DNS Poisoning Detection...")
    suspicious_responses = detect_dns_poisoning()
    if suspicious_responses:
        print(f"Detected {len(suspicious_responses)} suspicious DNS responses.")
        generate_pdf_report(suspicious_responses)
    else:
        print("No suspicious DNS responses detected.")

if __name__ == "__main__":
    main()
