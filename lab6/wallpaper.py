def calculate_wallpaper(area, price_per_roll):
    rolls_needed = area / 5  # Предположим, что один рулон покрывает 5 м²
    total_cost = rolls_needed * price_per_roll
    return rolls_needed, total_cost
