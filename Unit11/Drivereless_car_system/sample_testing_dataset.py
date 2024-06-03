{
  "routes": [
    {
      "route_name": "Default Route",
      "waypoints": ["Start", "Interim Point", "Default Destination"]
    },
    {
      "route_name": "Scenic Route",
      "waypoints": ["Start", "Scenic View", "Lake"]
    },
    {
      "route_name": "City Route",
      "waypoints": ["Start", "Downtown", "Office"]
    }
  ],
  "obstacles": [
    {
      "type": "Pedestrian",
      "proximity": 5
    },
    {
      "type": "Car",
      "proximity": 30
    },
    {
      "type": "Animal",
      "proximity": 15
    }
  ]
}
