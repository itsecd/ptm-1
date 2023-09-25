from collections import defaultdict


class Leaderboard(object):

    def __init__(self, races) -> None:
        self.races = races

    def driver_points(self) -> list:
        driver_points = defaultdict(int)
        for race in self.races:
            for driver in race.results:
                name = race.driver_name(driver)
                driver_points[name] += race.points(driver)
        return driver_points

    def driver_rankings(self) -> list:
        rankings = sorted(self.driver_points().items(),
                          key=lambda x: x[1], reverse = True)
        return [name for (name, points) in rankings]


class Driver(object):
    def __init__(self, name: str, country: str) -> None:
        self.name = name
        self.country = country


class SelfDrivingCar(Driver):
    def __init__(self, algorithm_version: str, company: str) -> None:
        Driver.__init__(self, None, company)
        self.algorithm_version = algorithm_version


class Race(object):

    _points = [25, 18, 15]

    def __init__(self, name: str, results: list) -> None:
        self.name = name
        self.results = results
        self.driver_names = {}
        for driver in results:
            name = driver.name
            if isinstance(driver, SelfDrivingCar):
                name = "Self Driving Car - {} ({})".format(
                    driver.country, driver.algorithm_version)
            self.driver_names[driver] = name

    def points(self, driver: int) -> list:
        return Race._points[self.results.index(driver)]

    def driver_name(self, driver: int) -> dict:
        return self.driver_names[driver]
