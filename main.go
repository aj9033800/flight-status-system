package main

import (
    "encoding/json"
    "net/http"
)

func getFlightStatus() string {
    return "On Time"
}

func flightStatusHandler(w http.ResponseWriter, r *http.Request) {
    status := getFlightStatus()
    jsonResponse, _ := json.Marshal(map[string]string{"status": status})
    w.Header().Set("Content-Type", "application/json")
    w.Write(jsonResponse)
}

func main() {
    http.HandleFunc("/api/flight/status", flightStatusHandler)
    http.ListenAndServe(":8080", nil)
}
