import datetime
from typing import List, Optional

from flask import Flask, request

app = Flask(__name__)


@app.route(
    "/search/", methods=["GET"],
)
def search():
    cell_tower_ids: List[int] = request.args.getlist("cell_tower_id", type=int)

    if not cell_tower_ids:
        return f"You must specify at least one cell_tower_id", 400

    for tower in cell_tower_ids:
        if tower <= 0:
            return f"cell_tower_id not be zero or less", 400

    phone_prefixes: List[str] = request.args.getlist("phone_prefix")
    for prefix in phone_prefixes:
        if prefix[-1] != "*" or len(prefix) > 10:
            return f"prefix must contain * and have less then 10 signs", 400

    protocols: List[str] = request.args.getlist("protocol")
    for protocol in protocols:
        if protocol != "2G" and protocol != "3G" and protocol != "4G":
            return f"protocol must be 2G, 3G or 4G", 400

    signal_level: Optional[float] = request.args.get(
        "signal_level", type=float, default=None
    )

    date_from: Optional[str] = request.args.get("date_from",default=None)
    if date_from:
        try:
            datetime.datetime.strptime(date_from, "%Y%m%d")
        except ValueError:
            return f"date_from wrong format", 400

    date_to: Optional[str] = request.args.get("date_to", default=None)
    if date_to:
        try:
            datetime.datetime.strptime(date_to, "%Y%m%d")
        except ValueError:
            return f"date_to wrong format", 400

    if date_from and date_to:
        now = datetime.datetime.now()
        try:
            to_date = datetime.datetime.strptime(date_to, "%Y%m%d")
            from_date = datetime.datetime.strptime(date_from, "%Y%m%d")
            if not now > to_date > from_date:
                return f"date wrong calculate", 400
        except ValueError:
            return f"date wrong format", 400

    numbers_sum_product: List[int] = request.args.getlist("numbers", type=int)
    summa = 0
    product = 1
    if numbers_sum_product:
        for number in numbers_sum_product:
            summa += number
            product *= number

    nums_a: List[int] = request.args.getlist("numbers_a", type=int)
    nums_b: List[int] = request.args.getlist("numbers_b", type=int)
    sum_nums = []
    for num_a in nums_a:
        for num_b in nums_b:
            sum_nums.append(str(num_a)+":"+str(num_b))
    for num_b in nums_b:
        for num_a in nums_a:
            sum_nums.append(str(num_b)+":"+str(num_a))

    numbers_a: List[int] = request.args.getlist("nums_a", type=int)
    x: [int] = request.args.get("x", type=int)
    numbers_a.sort()
    final_num = 0
    prev_num = 0
    for num in numbers_a:
        if num < x:
            prev_num = num
        else:
            if num-x < x-prev_num:
                final_num = num
            else:
                final_num = prev_num

    return (
        f"Search for {cell_tower_ids} cell towers. Search criteria: "
        f"phone_prefixes={phone_prefixes}, "
        f"protocols={protocols}, "
        f"signal_level={signal_level}"
        f"date_from={date_from}"
        f"date_to={date_to}"
        f"sum massive={summa}"
        f"product massive={product}"
        f"combinations a and b ={sum_nums}"
        f"closely X ={final_num}"
    )


if __name__ == "__main__":
    app.run(debug=True)
