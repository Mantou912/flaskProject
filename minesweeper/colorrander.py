from random import randint


class ColorRander:
    # BaseColor的内容中每个子元组代表一种色调的颜色
    # 每个子元组中, 存放同一种色调但深浅度不同的颜色
    BaseColor = (
        (
            "#750000",
            "#930000",
            "#AE0000",
            "#CE0000",
            "#EA0000",
        ),
        (
            "#BF0060",
            "#D9006C",
            "#F00078",
            "#FF0080",
            "#FF359A",
        ),
        (
            "#930093",
            "#AE00AE",
            "#D200D2",
            "#E800E8",
            "#FF00FF",
        ),
        (
            "#5B00AE",
            "#6F00D2",
            "#8600FF",
            "#921AFF",
            "#9F35FF",
        ),
        (
            "#0000C6",
            "#0000E3",
            "#2828FF",
            "#4A4AFF",
            "#6A6AFF",
        ),
        (
            "#005AB5",
            "#0066CC",
            "#0072E3",
            "#0080FF",
            "#2894FF",
        ),
        (
            "#009393",
            "#00AEAE",
            "#00CACA",
            "#00E3E3",
            "#00FFFF",
        ),
        (
            "#01B468",
            "#02C874",
            "#02DF82",
            "#02F78E",
            "#1AFD9C",
        ),
        (
            "#00A600",
            "#00BB00",
            "#00DB00",
            "#00EC00",
            "#28FF28",
        ),
        # ('#73BF00','#82D900','#8CEA00','#9AFF02','#A8FF24',),
        # ('#8C8C00','#A6A600','#C4C400','#E1E100','#F9F900',),
        (
            "#AE8F00",
            "#C6A300",
            "#D9B300",
            "#EAC100",
            "#FFD306",
        ),
        (
            "#D26900",
            "#EA7500",
            "#FF8000",
            "#FF9224",
            "#FFA042",
        ),
        (
            "#BB3D00",
            "#D94600",
            "#F75000",
            "#FF5809",
            "#FF8040",
        ),
    )

    def __init__(self) -> None:
        self.__colors = len(ColorRander.BaseColor)
        self.__kinds = len(ColorRander.BaseColor[0])
        self.__counts = {
            "sum": 0,
            "colors": [0] * self.__colors,
            "kinds": [[0] * self.__kinds for i in range(self.__colors)],
        }

    def rand_color(self) -> str:
        """尽可能有区分度且不重复地随机得到一种颜色"""
        choosen_color, choosen_kind = 0, 0

        # 优先保证每一种色调的颜色出现次数平均
        index = randint(0, self.__colors - 1)
        threshold = self.__counts["sum"] // self.__colors
        while True:
            if self.__counts["colors"][index] <= threshold:
                choosen_color = index
                break
            index = (index + 1) % self.__colors

        # 保证同一种色调不同深浅的颜色出现次数平均
        index = randint(0, self.__kinds - 1)
        threshold = self.__counts["colors"][choosen_color] // self.__kinds
        while True:
            if self.__counts["kinds"][choosen_color][index] <= threshold:
                choosen_kind = index
                break
            index = (index + 1) % self.__kinds

        self.__counts["sum"] += 1
        self.__counts["colors"][choosen_color] += 1
        self.__counts["kinds"][choosen_color][choosen_kind] += 1

        return ColorRander.BaseColor[choosen_color][choosen_kind]
