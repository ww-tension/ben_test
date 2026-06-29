# === Stage 9: Добавь импорт начальных данных из JSON-строки ===
# Project: StockMoves
def load_initial_data(json_string):
    import json
    try:
        data = json.loads(json_string)
        if not isinstance(data, dict):
            raise ValueError("JSON должен содержать объект")
        
        products = {}
        for item in data.get('products', []):
            pid = item['id']
            name = item['name']
            price = float(item['price'])
            batch_size = int(item.get('batch_size', 0))
            cost_price = float(item.get('cost_price', price * 0.9))
            
            if pid not in products:
                products[pid] = {
                    'name': name,
                    'price': price,
                    'batches': []
                }
            
            # Добавляем начальную партию как приход
            batch_id = f"BATCH_{len(products[pid]['batches']) + 1}"
            products[pid]['batches'].append({
                'id': batch_id,
                'quantity': batch_size,
                'cost_price': cost_price,
                'date': item.get('date', ''),
                'type': 'IN'
            })
        
        return {
            'products': products,
            'metadata': data.get('metadata', {})
        }
    except json.JSONDecodeError as e:
        print(f"Ошибка парсинга JSON: {e}")
        raise
