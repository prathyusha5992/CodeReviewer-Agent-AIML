def review_code(code):

    review = []

    # Avoid print statements
    if "print(" in code:
        review.append("⚠️ Avoid using print() statements in production code.")

    # TODO comments
    if "TODO" in code:
        review.append("⚠️ There are TODO comments that should be completed.")

    # Bare except block
    if "except:" in code:
        review.append("⚠️ Avoid using a bare except block. Catch specific exceptions.")

    # eval() usage
    if "eval(" in code:
        review.append("🚨 Security Risk: Avoid using eval().")

    # pass statement
    if "pass" in code:
        review.append("⚠️ 'pass' statement found. Consider implementing the required functionality.")

    # Wildcard imports
    if "import *" in code:
        review.append("⚠️ Avoid wildcard imports. Import only the required modules.")

    # Infinite loop
    if "while True" in code:
        review.append("⚠️ Infinite loop detected. Ensure there is a proper exit condition.")

    # Debug mode
    if "debug=True" in code:
        review.append("⚠️ Debug mode is enabled. Disable it before deploying.")

    # Hardcoded password
    if "password =" in code or "PASSWORD =" in code:
        review.append("🚨 Hardcoded password detected. Store sensitive information securely.")

    # FIXME comments
    if "FIXME" in code:
        review.append("⚠️ FIXME comments found. Resolve pending issues before production.")

    # Generic exception
    if "raise Exception" in code:
        review.append("⚠️ Avoid raising generic exceptions. Raise specific exception types.")

    # Long lines
    lines = code.split("\n")

    for i, line in enumerate(lines):
        if len(line) > 100:
            review.append(f"⚠️ Line {i+1} is longer than 100 characters.")

    # Empty file
    if len(code.strip()) == 0:
        review.append("⚠️ Empty file detected.")

    # If no issues found
    if not review:
        review.append("✅ No obvious issues found.")
        review.append("✅ Code structure looks good.")
        review.append("✅ Code follows basic best practices.")
        review.append("✅ Great job!")

    return "\n".join(review)