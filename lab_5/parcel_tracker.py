"""Demonstrate parcel booking, tracking, delivery status, and costs."""

from datetime import date
import secrets

STATUS_FLOW = (
    "Booked",
    "Picked Up",
    "In Transit",
    "Out for Delivery",
    "Delivered",
)
PARCELS = {}


def book_parcel(sender, receiver, weight_kg, history=None):
    """Book a parcel and optionally record its tracking ID in history."""
    if history is None:
        history = []

    tracking_id = f"TRK{10001 + len(PARCELS)}"
    PARCELS[tracking_id] = {
        "sender": sender,
        "receiver": receiver,
        "weight": weight_kg,
        "status": 0,
        "booked": str(date.today()),
    }
    history.append(tracking_id)
    return tracking_id


def advance_status(tracking_id):
    """Move a known parcel forward by one step and return its status."""
    parcel = PARCELS[tracking_id]
    if parcel["status"] < len(STATUS_FLOW) - 1:
        parcel["status"] += 1
    return STATUS_FLOW[parcel["status"]]


def shipping_cost(weight_kg):
    """Calculate shipping cost using the base rate and per-kilogram rate."""
    cost = 50
    if weight_kg > 1:
        cost += (weight_kg - 1) * 30
    return round(cost, 2)


def track_parcel(tracking_id):
    """Return a parcel route and status, or a message for an unknown ID."""
    parcel = PARCELS.get(tracking_id)
    if parcel is None:
        return f"Unknown tracking id {tracking_id}"

    route = f"{parcel['sender']} -> {parcel['receiver']}"
    return f"{route}: {STATUS_FLOW[parcel['status']]}"


def is_with_courier(tracking_id):
    """Return whether a parcel is picked up or in transit."""
    status = STATUS_FLOW[PARCELS[tracking_id]["status"]]
    return status in {"Picked Up", "In Transit"}


def main():
    """Run a short demonstration of the parcel tracker."""
    first = book_parcel("Bengaluru Books", "Ravi Kumar", 2.5)
    second = book_parcel("Gadget Hub", "Sneha Rao", 0.8)
    third = book_parcel("Spice Store", "Imran Khan", 4)
    advance_status(first)
    advance_status(first)
    advance_status(second)
    for _ in range(6):
        advance_status(third)

    for tracking_id in (first, second, third):
        print(track_parcel(tracking_id))
        print("  with courier:", is_with_courier(tracking_id))
        print("  cost:", shipping_cost(PARCELS[tracking_id]["weight"]))

    print(track_parcel("TRK00000"))  # unknown ID
    delivery_otp = secrets.randbelow(9000) + 1000
    print("Delivery OTP for", third, "is", delivery_otp)
    print("Parcels booked today:", len(PARCELS))


if __name__ == "__main__":
    main()
