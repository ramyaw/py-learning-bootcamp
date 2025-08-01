def retry_count_str(raw):
    try:
        return int(raw)
    except ValueError:
        return -1

print(retry_count_str("3"))    # 3
print(retry_count_str("none")) # -1
