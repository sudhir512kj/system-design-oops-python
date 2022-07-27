from abc import ABC, ABCMeta
from datetime import datetime
from enum import Enum
from shutil import move
from typing import List
# from customer import Customer


class Genre(Enum):
    COMEDY = 1
    ACTION = 2
    ROMANTIC = 3
    HORROR = 4


class SeatStatus(Enum):
    AVAILABLE = 1
    RESERVED = 2
    BOOKED = 3


class Gender(Enum):
    MALE = 1
    FEMALE = 2


class MovieRating(Enum):
    U = 1
    UA = 2
    A = 3
    S = 4


class BookingStatus(Enum):
    REQUESTED = 1
    CONFIRMED = 2
    CANCELLED = 3


class Address:
    def __init__(self, addressId: int, name: str, city: str, state: str, pin: str, contact: str) -> None:
        self.name = name
        self.city = city
        self.state = state
        self.pin = pin
        self.contact = contact
        newAddress = {
            "addressId": addressId,
            "name": name,
            "city": city,
            "state": state,
            "pin": pin,
            "contact": contact
        }
        addresses.append(newAddress)


# class Audi:
#     def __init__(self, audiName: str, shows: List[Show], totalSeats: int) -> None:
#         self.audiId: int = 0
#         self.audiName: str = audiName
#         self.shows: List[Show] = shows
#         self.totalSeats: int = totalSeats


class Seat:
    def __init__(self, status: SeatStatus) -> None:
        self.id = 0
        self.status = status

    def get_status(self):
        return self.status


class BoxSeat(Seat):
    def __init__(self, cost: int) -> None:
        super().__init__()
        self.cost = cost

    def __repr__(self) -> str:
        return super().__repr__()


class GoldSeat(Seat):
    def __init__(self, cost: int, status: BookingStatus) -> None:
        super().__init__(status)
        self.cost = cost


class Movie:
    def __init__(self, movieId: int, title: str, releaseDate: datetime, duration: int, lang: str, movieType: Genre, movieRating: MovieRating) -> None:
        self.movieId = movieId
        self.title = title
        self.releaseDate = releaseDate
        self.duration = duration
        self.language = lang
        self.movieType = movieType
        self.movieRating = movieRating
        newMovie = {
            "movieId": movieId,
            "title": title,
            "releaseDate": releaseDate,
            "duration": duration,
            "language": lang,
            "movieType": movieType.name,
            "movieRating": movieRating.name
        }
        movies.append(newMovie)

    def __repr__(self) -> str:
        return "Name : {}, Release Date: {}".format(self.title, self.releaseDate)


class Payment:
    def __init__(self, amount: float, date: datetime, transactionId: int) -> None:
        self.amount = amount
        self.date = date
        self.transactionId = transactionId


class Theater:
    def __init__(self, address: Address) -> None:
        self.address = address
        # self.audi = []
        self.movies = []
        newTheater = {
            "address": address,
            "movies": []
        }
        theaters.append(newTheater)

    def getMovies(self, dateList: List[datetime]) -> dict[datetime, Movie]:
        pass

    def getShows(self, dateList: List[datetime]) -> dict[datetime, Movie]:
        pass


class BookMyShow:
    def __init__(self, theaters: List[Theater] = []) -> None:
        self.theaters = theaters

    def getMovies(self, date: datetime, city: str) -> List[Movie]:
        pass

    def getCinemas(self, city: str) -> List[Theater]:
        pass


class Show:
    def __init__(self, showId: int, movieName: Movie, showTime: any, availableSeats: int, theater: Theater) -> None:
        self.showId = showId
        self.movieName = movieName
        self.showTime = showTime
        self.availableSeats = availableSeats
        self.theater = theater
        newShow = {
            "showId": showId,
            "movieName": movieName,
            "showTime": showTime,
            "availableSeats": availableSeats,
            "theater": theater,
            "city": theater.address.city
        }
        shows.append(newShow)


class Person(ABC):
    def __init__(self, userId: int, name: str, address: any, mobile: str, gender: any) -> None:
        super().__init__()
        self.userId = userId
        # self.obj = ''
        self.name = name
        self.address = address
        self.mobile = mobile
        self.gender = gender


class Customer(Person):
    def __init__(self, customerId: int, name: str, address: any, mobile: str, gender: any) -> None:
        super().__init__(customerId, name, address, mobile, gender)
        newCustomer = {
            "customerId": customerId,
            "name": name,
            "address": address,
            "mobile": mobile,
            "gender": gender,
            "bookings": []
        }
        customers.append(newCustomer)

    def getMoviesByTitle(self, title: str) -> any:
        return list(filter(lambda x: x["title"] == title, movies))

    def getMoviesByGenre(self, genre) -> any:
        return list(filter(lambda x: x["movieType"] == genre.name, movies))

    def getMoviesByCity(self, city) -> List[any]:
        showsInCity = list(filter(lambda x: x["city"] == city, shows))
        result = []
        for k in showsInCity:
            result.append(k["movieName"])
        return result

    def getMoviesByLanguage(self, language) -> any:
        return list(filter(lambda x: x["language"] == language, movies))

    def makeBooking(self, booking) -> None:
        show = list(
            filter(lambda item: item["showId"] == booking.bookedShow.showId, shows))
        idx = shows.index(show[0])
        shows[idx]["availableSeats"] -= 1
        booking2 = list(
            filter(lambda item: item["customerName"].userId == self.userId, bookings))
        idx = bookings.index(booking2[0])
        customers[idx]["bookings"].append(booking.bookingId)
        bookings[idx]["bookings"] = BookingStatus.CONFIRMED

    def cancelBooking(self, booking):
        booking2 = list(
            filter(lambda item: item["bookingId"] == booking.bookingId, bookings))
        idx = bookings.index(booking2[0])
        customers[idx]["bookings"] = BookingStatus.CANCELLED

    def getBooking(self) -> List[any]:
        res = list(
            filter(lambda item: item["customerName"].userId == self.userId, bookings))
        return res


class Booking:
    def __init__(self, bookingId: int, bookedShow: Show, bookingDate: datetime, customerName: Customer,
                 bookingStatus: BookingStatus, totalAmount: float, bookedSeat: List[Seat], paymentObj: Payment) -> None:
        self.bookingId = bookingId
        self.bookedShow = bookedShow
        self.bookingDate = bookingDate
        self.customerName = customerName
        # self.audi = audi
        self.bookingStatus = bookingStatus
        self.totalAmount = totalAmount
        self.bookedSeat = bookedSeat
        self.paymentObj = paymentObj

        newBooking = {
            "bookingId": bookingId,
            "bookedShow": bookedShow,
            "bookingDate": bookingDate,
            "customerName": customerName,
            # audi: audi
            "bookingStatus": bookingStatus,
            "totalAmount": totalAmount,
            "bookedSeat": bookedSeat,
            "paymentObj": paymentObj
        }
        bookings.append(newBooking)

    def makePayment(self, paymentObj: Payment) -> bool:
        try:
            newPayment = {
                "amount": paymentObj.amount,
                "date": paymentObj.date,
                "transactionId": paymentObj.transactionId
            }
            payments.append(newPayment)
            return True
        except:
            return False
    def __repr__(self) -> str:
        return "Name: {}, Mobile: {}, Show Details:-> Movie Name: {} Show Time: {}, Booking Status: {}, Amount: {}".format(
            self.customerName.name, self.customerName.mobile, self.bookedShow.movieName.title, self.bookedShow.showTime,
            self.bookingStatus.name, self.totalAmount
        )


if __name__ == '__main__':
    customers, customerCount = list(), 0
    theaters, theaterCount = list(), 0
    bookings, bookingCount = list(), 0
    addresses, addressCount = list(), 0
    movies, movieCount = list(), 0
    shows, showCount = list(), 0
    payments, paymentCount = list(), 0
    movie1 = Movie(movieCount := movieCount+1, "Iron Man",
                   datetime.now(), 180, "English", Genre.ACTION, MovieRating.U)
    movie2 = Movie(movieCount := movieCount+1, "Thor: Love and Thunder",
                   datetime.now(), 180, "English", Genre.ACTION, MovieRating.U)
    customer_address = Address(addressCount := addressCount+1,
                               "sudhir", "Ajmer", "Rajasthan", "305005", "9414400000")
    theater_address = Address(addressCount := addressCount+1,
                              "PVR Cinema", "Ajmer", "Rajasthan", "305005", "9414400089")
    pvr_grip = Theater(theater_address)
    # gender = Gender()
    show1 = Show(showCount := showCount+1, movie1,
                 datetime(2022, 8, 10), 25, pvr_grip)
    show2 = Show(showCount := showCount+1, movie2,
                 datetime(2022, 8, 12), 25, pvr_grip)
    sudhir = Customer(customerCount := customerCount+1, "Sudhir Meena", customer_address,
                      "9414400000", Gender.MALE)
    print(sudhir.getMoviesByTitle("Iron Man"))
    print(sudhir.getMoviesByGenre(Genre.ACTION))
    print(sudhir.getMoviesByLanguage("English"))
    print(sudhir.getMoviesByCity("Ajmer"))

    seat1 = GoldSeat(450, SeatStatus.AVAILABLE)
    payObj1 = Payment(450.00, datetime.now(), '202207270740sudhir512')
    booking1 = Booking(bookingCount := bookingCount+1, show1, datetime.now(),
                       sudhir, BookingStatus.REQUESTED, 450.00, seat1, payObj1)
    payObj2 = Payment(450.00, datetime.now(), '202207270940sudhir512')
    booking2 = Booking(bookingCount := bookingCount+1, show1, datetime.now(),
                       sudhir, BookingStatus.REQUESTED, 450.00, seat1, payObj2)
    booking1Payment = booking1.makePayment(payObj1)
    if booking1Payment:
        sudhir.makeBooking(booking1)
    else:
        sudhir.cancelBooking(booking1)
    booking2Payment = booking1.makePayment(payObj2)
    if booking2Payment:
        sudhir.makeBooking(booking2)
    else:
        sudhir.cancelBooking(booking2)
    sudhir.makeBooking(booking2)
    print(sudhir.getBooking())
