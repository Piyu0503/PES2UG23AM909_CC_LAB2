from locust import HttpUser, task, between

class MyEventsUser(HttpUser):
    # Reduced wait time to increase throughput
    wait_time = between(0.2, 0.5)

    @task
    def view_my_events(self):
        with self.client.get(
            "/my-events",
            headers={"Connection": "keep-alive"},
            catch_response=True
        ) as response:
            if response.status_code != 200:
                response.failure("Failed to load my-events")
