from rest_framework import serializers

class BookSerializer(serializers.Serializer):
    id=serializers.IntegerField(label="Enter Book Id")
    title=serializers.CharField(label="Enter Book Title")
    author=serializers.CharField(label="Enter Author Names")
    
    
    
class ProductSerializer(serializers.Serializer):
    product_name = serializers.CharField()
    category = serializers.CharField()
    subcategory = serializers.CharField()
    price = serializers.IntegerField()
    desc = serializers.CharField()
    image = serializers.ImageField()  # No `upload_to` argument here

    # If you need to handle additional logic, consider using validation methods
    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError("Price must be greater than zero.")