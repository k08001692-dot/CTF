users = [
    {
        "id": 1,
        "email": "user@bookhaven.com",
        "password": "password123",
        "role": "user"
    },
    {
        "id": 2,
        "email": "admin@bookhaven.com",
        "password": "admin123",
        "role": "admin"
    }
]

orders = [
    {
        "id": 1001,
        "user_id": 1,
        "items": ["The Silent Algorithm"],
        "total": 499,
        "status": "delivered"
    },
    {
        "id": 1002,
        "user_id": 2,
        "items": ["Hidden Pages", "Pastel Secrets"],
        "total": 698,
        "status": "processing",
        "metadata": {
            "internal_note": "FLAG{objects_dont_belong_to_you}",
            "priority": "high"
        }
    }
]

wishlists = {
    1: {
        "user_id": 1,
        "items": ["Pastel Secrets"],
        "private_notes": "birthday gift idea"
    },
    2: {
        "user_id": 2,
        "items": ["The Silent Algorithm"],
        "private_notes": "FLAG{blind_access_is_still_access}",
        "internal": {"preferences": {"notify": True}}
    }
}

sessions = {}

books = [
    {
        "id": 1,
        "title": "The Silent Algorithm",
        "price": 499
    },
    {
        "id": 2,
        "title": "Pastel Secrets",
        "price": 399
    },
    {
        "id": 3,
        "title": "Hidden Pages",
        "price": 299
    }
]
