from concurrent import futures
import grpc
import sys
from proto import restaurant_pb2
from proto import restaurant_pb2_grpc

# Menu categories
RESTAURANT_ITEMS_FOOD = ["chips", "fish", "burger", "pizza", "pasta", "salad"]
RESTAURANT_ITEMS_DRINK = ["water", "fizzy drink", "juice", "smoothie", "coffee", "beer"]
RESTAURANT_ITEMS_DESSERT = ["ice cream", "chocolate cake", "cheese cake", "brownie", "pancakes", "waffles"]


class Restaurant(restaurant_pb2_grpc.RestaurantServicer):

    def DrinkOrder(self, request, context):
        items_status = all(item in RESTAURANT_ITEMS_DRINK for item in request.items)
        status = restaurant_pb2.RestaurantResponse.ACCEPTED if items_status else restaurant_pb2.RestaurantResponse.REJECTED
        item_message = [restaurant_pb2.items(itemName=item) for item in request.items]
        return restaurant_pb2.RestaurantResponse(orderID=request.orderID, status=status, itemMessage=item_message)

    def FoodOrder(self, request, context):
        items_status = all(item in RESTAURANT_ITEMS_FOOD for item in request.items)
        status = restaurant_pb2.RestaurantResponse.ACCEPTED if items_status else restaurant_pb2.RestaurantResponse.REJECTED
        item_message = [restaurant_pb2.items(itemName=item) for item in request.items]
        return restaurant_pb2.RestaurantResponse(orderID=request.orderID, status=status, itemMessage=item_message)

    def DessertOrder(self, request, context):
        items_status = all(item in RESTAURANT_ITEMS_DESSERT for item in request.items)
        status = restaurant_pb2.RestaurantResponse.ACCEPTED if items_status else restaurant_pb2.RestaurantResponse.REJECTED
        item_message = [restaurant_pb2.items(itemName=item) for item in request.items]
        return restaurant_pb2.RestaurantResponse(orderID=request.orderID, status=status, itemMessage=item_message)

    def MealOrder(self, request, context):
        # Check that the order has exactly one item from each category in the correct order
        if (len(request.items) == 3 and
                request.items[0] in RESTAURANT_ITEMS_FOOD and
                request.items[1] in RESTAURANT_ITEMS_DRINK and
                request.items[2] in RESTAURANT_ITEMS_DESSERT):
            status = restaurant_pb2.RestaurantResponse.ACCEPTED
        else:
            status = restaurant_pb2.RestaurantResponse.REJECTED

        item_message = [restaurant_pb2.items(itemName=item) for item in request.items]
        return restaurant_pb2.RestaurantResponse(orderID=request.orderID, status=status, itemMessage=item_message)


def serve():
    port = 'localhost:{0}'.format(sys.argv[1])
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    restaurant_pb2_grpc.add_RestaurantServicer_to_server(Restaurant(), server)
    server.add_insecure_port(port)
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
