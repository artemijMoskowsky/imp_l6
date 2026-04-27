from typing import List
import unittest


def find_available_medicines(
        pharmacies: List[dict],
        medicine: str) -> List[str]:
    """
    Функція для визначеня у яких аптеках є препарат.
    Повертає список назв аптек.
    """
    result = []

    for pharmacy in pharmacies:
        if medicine in pharmacy.get("medicines", []):
            result.append(pharmacy["name"])

    return result


def main():
    pharmacies = [
        {
            "name": "Аптека 1",
            "medicines": ["Аспірин", "Парацетамол"]
        },
        {
            "name": "Аптека 2",
            "medicines": ["Ібупрофен"]
        },
        {
            "name": "Аптека 3",
            "medicines": ["Аспірин", "Нурофен"]
        },
        {
            "name": "Аптека 5",
            "medicines": ["Парацетамол", "Ібупрофен"]
        }
    ]
    print(
        "Аптеки що мають препарат:",
        ", ".join(
            find_available_medicines(
                pharmacies,
                "Ібупрофен")))

# UNIT TESTS


class PharmacyUnitTests(unittest.TestCase):
    def test_find_available_medicines(self):
        records = [
            {
                "name": "Аптека 1",
                "medicines": ["Аспірин", "Парацетамол"]
            },
            {
                "name": "Аптека 2",
                "medicines": ["Ібупрофен"]
            }
        ]
        expected = [
            "Аптека 2"
        ]
        self.assertEqual(
            find_available_medicines(
                records,
                "Ібупрофен"),
            expected)

    def test_empty(self):
        records = []
        expected = []
        self.assertEqual(
            find_available_medicines(
                records,
                "Ібупрофен"),
            expected)

    def test_find_available_medicines2(self):
        records = [
            {
                "name": "Аптека 1",
                "medicines": ["Аспірин", "Ібупрофен"]
            },
            {
                "name": "Аптека 2",
                "medicines": ["Аспірин"]
            },
            {
                "name": "Аптека 3",
                "medicines": ["Парацетамол"]
            }
        ]
        expected = [
            "Аптека 1",
            "Аптека 2"
        ]
        self.assertEqual(find_available_medicines(records, "Аспірин"),
                         expected)


if __name__ == "__main__":
    main()

    unittest.main()
