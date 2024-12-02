import dataclasses
from typing import Callable, Generator, Iterable, NewType, Sequence, TypeVar

DEBUG = True

UserDataDict = dict[str, str | int]

Celsius = NewType("Celsius", float)
Fareng = NewType("Fareng", float)


def convert_cels_to_faren(temp: Celsius) -> Fareng:
    return Fareng(temp * 9 / 5 + 32)


def get_max_temp(temps: Iterable[Celsius]) -> Celsius | None:
    if temps:
        return max(temps)
    return None


def get_first_temp(temps: Sequence[Celsius]) -> Celsius | None:
    if temps:
        return temps[0]
    return None


TempT = TypeVar("TempT")

def get_first_temp_generic(temps: Sequence[TempT]) -> TempT | None:
    if temps:
        return temps[0]
    return None


def gen_temps(delta: float) -> Generator[Celsius, None, str]:
    yield Celsius(7.0)
    yield Celsius(7.0 + delta)
    yield Celsius(7.0 + 2 * delta)

    return "end"  # StopIteration("end")


def run_temperatures() -> None:
    temp = Celsius(30.0)
    print(f"{isinstance(temp, float)=}, {type(temp)=}")

    temp_faren = convert_cels_to_faren(temp)
    print(f"{temp_faren=}, {type(temp_faren)=}")

    max_temp = get_max_temp(
        [Celsius(9.0), Celsius(1.0), Celsius(15.0)]
    )
    print(f"{max_temp=}")

    max_temp = get_max_temp(
        (Celsius(9.0), Celsius(1.0), Celsius(15.0))
    )
    print(f"{max_temp=}")

    max_temp = get_max_temp(
        gen_temps(19.0)
    )
    print(f"{max_temp=}")

    # first temp
    first_temp = get_first_temp(
        [Celsius(9.0), Celsius(1.0), Celsius(15.0)]
    )
    print(f"{first_temp=}")

    first_temp = get_first_temp(
        (Celsius(9.0), Celsius(1.0), Celsius(15.0))
    )
    print(f"{first_temp=}")

    # first_temp = get_first_temp(
    #     gen_temps(19.0)
    # )
    # print(f"{first_temp=}")

    # TempT
    res1 = get_first_temp_generic(
        [Celsius(9.0), Celsius(1.0), Celsius(15.0)]
    )
    print(f"{res1=}")

    input_tuple: tuple[int,...] = (1, 2, 3)
    res2 = get_first_temp_generic(
        input_tuple
    )
    print(f"{res2=}")

    res3 = get_first_temp_generic(
        [Fareng(9.0), Fareng(1.0), Fareng(15.0)]
    )
    print(f"{res3=}")



@dataclasses.dataclass
class User:
    user_id: int
    name: str


def make_request(url: str) -> UserDataDict:
    # make real http request
    return {
        "name": "Steve",
        "id": 654,
    }


def fetch_user_data(user: User) -> UserDataDict:
    if DEBUG:
        url = "https://python.org/123"
    else:
        url = "https://python.org/{user.user_id}"

    result = make_request(url)

    return result


def run_fetch() -> None:
    usr = User(456, "Steve")

    user_data: UserDataDict = fetch_user_data(usr)
    print(f"{user_data=}")


T = TypeVar("T")
M = TypeVar("M")

def add(x: T, y: M) -> tuple[M, T]:
    return (y, x)


def add_str(a: str, b: str) -> str:
    return a + b


def add_int(a: int, b: int) -> int:
    return a + b


def apply_operation(
    fn: Callable[[T, T], T],
    op1: T,
    op2: T,
) -> T:
    return fn(op1, op2)


def deco(fn: Callable[..., T]) -> Callable[..., T]:
    def inner(*args, **kwargs) -> T:
        return fn(*args, **kwargs)
    return inner


@deco
def for_deco(name: str) -> User:
    return User(123, name)


def deco_wrong(fn: Callable[..., T]) -> Callable[..., T]:
    def inner(*args, **kwargs) -> T:
        return fn(*args, **kwargs),
    return inner


@deco_wrong
def for_deco_invalid(name: str) -> User:
    return User(123, name)


def run_functions() -> None:
    res = add("1", 99)
    print(f"{res=}")

    res1: tuple[int, str] = add("1", 99)
    print(f"{res1=}")

    res2: tuple[list, dict] = add({}, [])
    print(f"{res2=}")

    # apply
    res_add_str = apply_operation(add_str, "qw", "35")
    print(f"{res_add_str=}")

    res_add_int = apply_operation(add_int, 35, 12)
    print(f"{res_add_int=}")

    res_add = apply_operation(add, "35", 12)
    print(f"{res_add=}")


if __name__ == "__main__":
    run_fetch()
    run_temperatures()
    run_functions()

