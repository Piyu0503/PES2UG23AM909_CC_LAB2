from locust import HttpUser, task, between

class EventsUser(HttpUser):
    # Reduced wait time → more realistic concurrent load
    wait_time = between(0.2, 0.5)

    @task
    def view_events(self):
        with self.client.get(
            "/events",
            headers={"Connection": "keep-alive"},
            catch_response=True
        ) as response:
            if response.status_code != 200:
                response.failure("Failed to load events")
