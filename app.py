from flask import Flask, request, jsonify
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

# Data penjualan pisang coklat untuk keperluan pengujian
sales = [
    {"id": 1, "product": "Pisang Coklat", "quantity": 10, "price": 15000, "date": "2024-11-01"},
    {"id": 2, "product": "Pisang Coklat", "quantity": 5, "price": 7500, "date": "2024-11-02"},
    {"id": 3, "product": "Pisang Coklat", "quantity": 7, "price": 10500, "date": "2024-11-03"},
    {"id": 4, "product": "Pisang Coklat", "quantity": 12, "price": 18000, "date": "2024-11-04"},
    {"id": 5, "product": "Pisang Coklat", "quantity": 6, "price": 9000, "date": "2024-11-05"},
    {"id": 6, "product": "Pisang Coklat", "quantity": 15, "price": 22500, "date": "2024-11-06"},
    {"id": 7, "product": "Pisang Coklat", "quantity": 8, "price": 12000, "date": "2024-11-07"},
    {"id": 8, "product": "Pisang Coklat", "quantity": 20, "price": 30000, "date": "2024-11-08"},
    {"id": 9, "product": "Pisang Coklat", "quantity": 4, "price": 6000, "date": "2024-11-09"},
    {"id": 10, "product": "Pisang Coklat", "quantity": 9, "price": 13500, "date": "2024-11-10"},
]

class SalesList(Resource):
    def get(self):
        return {
            "error": False,
            "message": "success",
            "count": len(sales),
            "sales": sales
        }

    def post(self):
        data = request.get_json()
        new_sale = {
            "id": len(sales) + 1,
            "product": data["product"],
            "quantity": data["quantity"],
            "price": data["price"],
            "date": data["date"]
        }
        sales.append(new_sale)
        return {"error": False, "message": "Sale added successfully", "sale": new_sale}, 201

class SalesDetail(Resource):
    def get(self, sale_id):
        sale = next((s for s in sales if s["id"] == sale_id), None)
        if sale:
            return {"error": False, "message": "success", "sale": sale}
        return {"error": True, "message": "Sale not found"}, 404

    def put(self, sale_id):
        data = request.get_json()
        sale = next((s for s in sales if s["id"] == sale_id), None)
        if sale:
            sale.update(data)
            return {"error": False, "message": "Sale updated successfully", "sale": sale}
        return {"error": True, "message": "Sale not found"}, 404

    def delete(self, sale_id):
        global sales
        sales = [s for s in sales if s["id"] != sale_id]
        return {"error": False, "message": "Sale deleted successfully"}, 200

# Tambahkan resources ke API
api.add_resource(SalesList, '/sales')
api.add_resource(SalesDetail, '/sales/<int:sale_id>')

if __name__ == "__main__":
    app.run(debug=True)
