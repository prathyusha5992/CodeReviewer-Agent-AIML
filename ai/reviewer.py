def review_code(code):

    review = []

    if "print(" in code:
        review.append("⚠️ Avoid using print() statements in production code.")

    if "TODO" in code:
        review.append("⚠️ There are TODO comments that should be completed.")

    if "except:" in code:
        review.append("⚠️ Avoid using a bare except block. Catch specific exceptions.")

    if "eval(" in code:
        review.append("🚨 Security Risk: Avoid using eval().")

    lines = code.split("\n")

    for i, line in enumerate(lines):
        if len(line) > 100:
            review.append(f"⚠️ Line {i+1} is longer than 100 characters.")

    if not review:
        review.append("✅ No obvious issues found.")
        review.append("✅ Code structure looks good.")
        review.append("✅ Great job!")

    return "\n".join(review)