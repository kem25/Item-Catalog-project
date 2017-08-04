from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from tdatabase_setup import Base,Country,VisitList

engine=create_engine('sqlite:///catalog.db')
Base.metadata.bind=engine
DBsession=sessionmaker(bind=engine)
session=DBsession()


country1=Country(name="United-States")
session.add(country1)
session.commit()


list1=VisitList(name= "Grand-Canyon", category="national-park", description="It  is a steep-sided" \
                "canyon carved by the Colorado River in Arizona, United States. The Grand Canyon" \
                "is 277 miles (446 km) long, up to 18 miles (29 km) wide and attains a depth of" \
                "over a mile (6,093 feet or 1,857 meters).The canyon and adjacent rim are contained" \
                "within Grand Canyon National Park, the Kaibab National Forest, Grand Canyon-Parashant" \
                "National Monument, the Hualapai Indian Reservation, the Havasupai Indian Reservation" \
                "and the Navajo Nation.", country= country1)
session.add(list1)
session.commit()

list2=VisitList(name= "Niagra-falls", category="national-park", description="It  is a steep-sided" \
                "canyon carved by the Colorado River in Arizona, United States. The Grand Canyon" \
                "is 277 miles (446 km) long, up to 18 miles (29 km) wide and attains a depth of" \
                "over a mile (6,093 feet or 1,857 meters).The canyon and adjacent rim are contained" \
                "within Grand Canyon National Park, the Kaibab National Forest, Grand Canyon-Parashant" \
                "National Monument, the Hualapai Indian Reservation, the Havasupai Indian Reservation" \
                "and the Navajo Nation.", country= country1)
session.add(list2)
session.commit()


list3=VisitList(name= "Disney-World", category="theme-park", description="It  is a steep-sided" \
                "canyon carved by the Colorado River in Arizona, United States. The Grand Canyon" \
                "is 277 miles (446 km) long, up to 18 miles (29 km) wide and attains a depth of" \
                "over a mile (6,093 feet or 1,857 meters).The canyon and adjacent rim are contained" \
                "within Grand Canyon National Park, the Kaibab National Forest, Grand Canyon-Parashant" \
                "National Monument, the Hualapai Indian Reservation, the Havasupai Indian Reservation" \
                "and the Navajo Nation.", country= country1)
session.add(list3)
session.commit()


list4=VisitList(name= "6-Flags", category="amusement-park", description="It  is a steep-sided" \
                "canyon carved by the Colorado River in Arizona, United States. The Grand Canyon" \
                "is 277 miles (446 km) long, up to 18 miles (29 km) wide and attains a depth of" \
                "over a mile (6,093 feet or 1,857 meters).The canyon and adjacent rim are contained" \
                "within Grand Canyon National Park, the Kaibab National Forest, Grand Canyon-Parashant" \
                "National Monument, the Hualapai Indian Reservation, the Havasupai Indian Reservation" \
                "and the Navajo Nation.", country= country1)
session.add(list4)
session.commit()


list5=VisitList(name= "White-house", category="historical-monument", description="It  is a steep-sided" \
                "canyon carved by the Colorado River in Arizona, United States. The Grand Canyon" \
                "is 277 miles (446 km) long, up to 18 miles (29 km) wide and attains a depth of" \
                "over a mile (6,093 feet or 1,857 meters).The canyon and adjacent rim are contained" \
                "within Grand Canyon National Park, the Kaibab National Forest, Grand Canyon-Parashant" \
                "National Monument, the Hualapai Indian Reservation, the Havasupai Indian Reservation" \
                "and the Navajo Nation.", country= country1)
session.add(list5)
session.commit()


country2=Country(name="India")
session.add(country2)
session.commit()


list92=VisitList(name= "Taj-Mahal", category="historical-monument", description="It  is a steep-sided" \
                "canyon carved by the Colorado River in Arizona, United States. The Grand Canyon" \
                "is 277 miles (446 km) long, up to 18 miles (29 km) wide and attains a depth of" \
                "over a mile (6,093 feet or 1,857 meters).The canyon and adjacent rim are contained" \
                "within Grand Canyon National Park, the Kaibab National Forest, Grand Canyon-Parashant" \
                "National Monument, the Hualapai Indian Reservation, the Havasupai Indian Reservation" \
                "and the Navajo Nation.", country= country2)
session.add(list92)
session.commit()

list82=VisitList(name= "Red-fort", category="historical-monument", description="It  is a steep-sided" \
                "canyon carved by the Colorado River in Arizona, United States. The Grand Canyon" \
                "is 277 miles (446 km) long, up to 18 miles (29 km) wide and attains a depth of" \
                "over a mile (6,093 feet or 1,857 meters).The canyon and adjacent rim are contained" \
                "within Grand Canyon National Park, the Kaibab National Forest, Grand Canyon-Parashant" \
                "National Monument, the Hualapai Indian Reservation, the Havasupai Indian Reservation" \
                "and the Navajo Nation.", country= country2)
session.add(list82)
session.commit()


list72=VisitList(name= "Charminar", category="historical-monument", description="It  is a steep-sided" \
                "canyon carved by the Colorado River in Arizona, United States. The Grand Canyon" \
                "is 277 miles (446 km) long, up to 18 miles (29 km) wide and attains a depth of" \
                "over a mile (6,093 feet or 1,857 meters).The canyon and adjacent rim are contained" \
                "within Grand Canyon National Park, the Kaibab National Forest, Grand Canyon-Parashant" \
                "National Monument, the Hualapai Indian Reservation, the Havasupai Indian Reservation" \
                "and the Navajo Nation.", country= country2)
session.add(list72)
session.commit()


list62=VisitList(name= "Water-world", category="amusement-park", description="It  is a steep-sided" \
                "canyon carved by the Colorado River in Arizona, United States. The Grand Canyon" \
                "is 277 miles (446 km) long, up to 18 miles (29 km) wide and attains a depth of" \
                "over a mile (6,093 feet or 1,857 meters).The canyon and adjacent rim are contained" \
                "within Grand Canyon National Park, the Kaibab National Forest, Grand Canyon-Parashant" \
                "National Monument, the Hualapai Indian Reservation, the Havasupai Indian Reservation" \
                "and the Navajo Nation.", country= country2)
session.add(list62)
session.commit()


list52=VisitList(name= "Kerala-backwaters", category="national-park", description="It  is a steep-sided" \
                "canyon carved by the Colorado River in Arizona, United States. The Grand Canyon" \
                "is 277 miles (446 km) long, up to 18 miles (29 km) wide and attains a depth of" \
                "over a mile (6,093 feet or 1,857 meters).The canyon and adjacent rim are contained" \
                "within Grand Canyon National Park, the Kaibab National Forest, Grand Canyon-Parashant" \
                "National Monument, the Hualapai Indian Reservation, the Havasupai Indian Reservation" \
                "and the Navajo Nation.", country= country2)
session.add(list52)
session.commit()


country3=Country(name="France")
session.add(country3)
session.commit()


list33=VisitList(name= "Eiffel-Tower", category="historical-monument", description="It  is a steep-sided" \
                "canyon carved by the Colorado River in Arizona, United States. The Grand Canyon" \
                "is 277 miles (446 km) long, up to 18 miles (29 km) wide and attains a depth of" \
                "over a mile (6,093 feet or 1,857 meters).The canyon and adjacent rim are contained" \
                "within Grand Canyon National Park, the Kaibab National Forest, Grand Canyon-Parashant" \
                "National Monument, the Hualapai Indian Reservation, the Havasupai Indian Reservation" \
                "and the Navajo Nation.", country= country3)
session.add(list33)
session.commit()

list37=VisitList(name= "The Louvre", category="historical-monument", description="It  is a steep-sided" \
                "canyon carved by the Colorado River in Arizona, United States. The Grand Canyon" \
                "is 277 miles (446 km) long, up to 18 miles (29 km) wide and attains a depth of" \
                "over a mile (6,093 feet or 1,857 meters).The canyon and adjacent rim are contained" \
                "within Grand Canyon National Park, the Kaibab National Forest, Grand Canyon-Parashant" \
                "National Monument, the Hualapai Indian Reservation, the Havasupai Indian Reservation" \
                "and the Navajo Nation.", country= country3)
session.add(list37)
session.commit()

list36=VisitList(name= "Arc-de-Triomphe", category="historical-monument", description="It  is a steep-sided" \
                "canyon carved by the Colorado River in Arizona, United States. The Grand Canyon" \
                "is 277 miles (446 km) long, up to 18 miles (29 km) wide and attains a depth of" \
                "over a mile (6,093 feet or 1,857 meters).The canyon and adjacent rim are contained" \
                "within Grand Canyon National Park, the Kaibab National Forest, Grand Canyon-Parashant" \
                "National Monument, the Hualapai Indian Reservation, the Havasupai Indian Reservation" \
                "and the Navajo Nation.", country= country3)
session.add(list36)
session.commit()

list35=VisitList(name= "Palace-of-Versailles", category="historical-monument", description="It  is a steep-sided" \
                "canyon carved by the Colorado River in Arizona, United States. The Grand Canyon" \
                "is 277 miles (446 km) long, up to 18 miles (29 km) wide and attains a depth of" \
                "over a mile (6,093 feet or 1,857 meters).The canyon and adjacent rim are contained" \
                "within Grand Canyon National Park, the Kaibab National Forest, Grand Canyon-Parashant" \
                "National Monument, the Hualapai Indian Reservation, the Havasupai Indian Reservation" \
                "and the Navajo Nation.", country= country3)
session.add(list35)
session.commit()

list23=VisitList(name= "Alps", category="national-park", description="It  is a steep-sided" \
                "canyon carved by the Colorado River in Arizona, United States. The Grand Canyon" \
                "is 277 miles (446 km) long, up to 18 miles (29 km) wide and attains a depth of" \
                "over a mile (6,093 feet or 1,857 meters).The canyon and adjacent rim are contained" \
                "within Grand Canyon National Park, the Kaibab National Forest, Grand Canyon-Parashant" \
                "National Monument, the Hualapai Indian Reservation, the Havasupai Indian Reservation" \
                "and the Navajo Nation.", country= country3)
session.add(list23)
session.commit()

country4=Country(name="Sweden")
session.add(country4)
session.commit()


list21=VisitList(name= "Skansen", category="historical-monument", description="It  is a steep-sided" \
                "canyon carved by the Colorado River in Arizona, United States. The Grand Canyon" \
                "is 277 miles (446 km) long, up to 18 miles (29 km) wide and attains a depth of" \
                "over a mile (6,093 feet or 1,857 meters).The canyon and adjacent rim are contained" \
                "within Grand Canyon National Park, the Kaibab National Forest, Grand Canyon-Parashant" \
                "National Monument, the Hualapai Indian Reservation, the Havasupai Indian Reservation" \
                "and the Navajo Nation.", country= country4)
session.add(list21)
session.commit()

list4=VisitList(name= "Vasa-Museum", category="historical-monument", description="It  is a steep-sided" \
                "canyon carved by the Colorado River in Arizona, United States. The Grand Canyon" \
                "is 277 miles (446 km) long, up to 18 miles (29 km) wide and attains a depth of" \
                "over a mile (6,093 feet or 1,857 meters).The canyon and adjacent rim are contained" \
                "within Grand Canyon National Park, the Kaibab National Forest, Grand Canyon-Parashant" \
                "National Monument, the Hualapai Indian Reservation, the Havasupai Indian Reservation" \
                "and the Navajo Nation.", country= country4)
session.add(list4)
session.commit()

list20=VisitList(name= "Drottningholm Palace", category="historical-monument", description="It  is a steep-sided" \
                "canyon carved by the Colorado River in Arizona, United States. The Grand Canyon" \
                "is 277 miles (446 km) long, up to 18 miles (29 km) wide and attains a depth of" \
                "over a mile (6,093 feet or 1,857 meters).The canyon and adjacent rim are contained" \
                "within Grand Canyon National Park, the Kaibab National Forest, Grand Canyon-Parashant" \
                "National Monument, the Hualapai Indian Reservation, the Havasupai Indian Reservation" \
                "and the Navajo Nation.", country= country4)
session.add(list20)
session.commit()

list19=VisitList(name= "Stockholm Palace", category="historical-monument", description="It  is a steep-sided" \
                "canyon carved by the Colorado River in Arizona, United States. The Grand Canyon" \
                "is 277 miles (446 km) long, up to 18 miles (29 km) wide and attains a depth of" \
                "over a mile (6,093 feet or 1,857 meters).The canyon and adjacent rim are contained" \
                "within Grand Canyon National Park, the Kaibab National Forest, Grand Canyon-Parashant" \
                "National Monument, the Hualapai Indian Reservation, the Havasupai Indian Reservation" \
                "and the Navajo Nation.", country= country4)
session.add(list4)
session.commit()

list4=VisitList(name= "Gamla stan", category="national-park", description="It  is a steep-sided" \
                "canyon carved by the Colorado River in Arizona, United States. The Grand Canyon" \
                "is 277 miles (446 km) long, up to 18 miles (29 km) wide and attains a depth of" \
                "over a mile (6,093 feet or 1,857 meters).The canyon and adjacent rim are contained" \
                "within Grand Canyon National Park, the Kaibab National Forest, Grand Canyon-Parashant" \
                "National Monument, the Hualapai Indian Reservation, the Havasupai Indian Reservation" \
                "and the Navajo Nation.", country= country4)
session.add(list19)
session.commit()


country5=Country(name="Canada")
session.add(country5)
session.commit()

list18=VisitList(name= "Banff National Park", category="national-park", description="It  is a steep-sided" \
                "canyon carved by the Colorado River in Arizona, United States. The Grand Canyon" \
                "is 277 miles (446 km) long, up to 18 miles (29 km) wide and attains a depth of" \
                "over a mile (6,093 feet or 1,857 meters).The canyon and adjacent rim are contained" \
                "within Grand Canyon National Park, the Kaibab National Forest, Grand Canyon-Parashant" \
                "National Monument, the Hualapai Indian Reservation, the Havasupai Indian Reservation" \
                "and the Navajo Nation.", country= country5)
session.add(list18)
session.commit()

list17=VisitList(name= "Jasper National Park", category="national-park", description="It  is a steep-sided" \
                "canyon carved by the Colorado River in Arizona, United States. The Grand Canyon" \
                "is 277 miles (446 km) long, up to 18 miles (29 km) wide and attains a depth of" \
                "over a mile (6,093 feet or 1,857 meters).The canyon and adjacent rim are contained" \
                "within Grand Canyon National Park, the Kaibab National Forest, Grand Canyon-Parashant" \
                "National Monument, the Hualapai Indian Reservation, the Havasupai Indian Reservation" \
                "and the Navajo Nation.", country= country5)
session.add(list17)
session.commit()

list16=VisitList(name= "Rocky-mountains", category="national-park", description="It  is a steep-sided" \
                "canyon carved by the Colorado River in Arizona, United States. The Grand Canyon" \
                "is 277 miles (446 km) long, up to 18 miles (29 km) wide and attains a depth of" \
                "over a mile (6,093 feet or 1,857 meters).The canyon and adjacent rim are contained" \
                "within Grand Canyon National Park, the Kaibab National Forest, Grand Canyon-Parashant" \
                "National Monument, the Hualapai Indian Reservation, the Havasupai Indian Reservation" \
                "and the Navajo Nation.", country= country5)
session.add(list16)
session.commit()

list15=VisitList(name= "Canadian Rockies", category="national-park", description="It  is a steep-sided" \
                "canyon carved by the Colorado River in Arizona, United States. The Grand Canyon" \
                "is 277 miles (446 km) long, up to 18 miles (29 km) wide and attains a depth of" \
                "over a mile (6,093 feet or 1,857 meters).The canyon and adjacent rim are contained" \
                "within Grand Canyon National Park, the Kaibab National Forest, Grand Canyon-Parashant" \
                "National Monument, the Hualapai Indian Reservation, the Havasupai Indian Reservation" \
                "and the Navajo Nation.", country= country5)
session.add(list15)
session.commit()

country6=Country(name="England")
session.add(country6)
session.commit()

list14=VisitList(name= "Tower of London", category="national-park", description="It  is a steep-sided" \
                "canyon carved by the Colorado River in Arizona, United States. The Grand Canyon" \
                "is 277 miles (446 km) long, up to 18 miles (29 km) wide and attains a depth of" \
                "over a mile (6,093 feet or 1,857 meters).The canyon and adjacent rim are contained" \
                "within Grand Canyon National Park, the Kaibab National Forest, Grand Canyon-Parashant" \
                "National Monument, the Hualapai Indian Reservation, the Havasupai Indian Reservation" \
                "and the Navajo Nation.", country= country6)
session.add(list14)
session.commit()

list13=VisitList(name= "Stonehenge", category="national-park", description="It  is a steep-sided" \
                "canyon carved by the Colorado River in Arizona, United States. The Grand Canyon" \
                "is 277 miles (446 km) long, up to 18 miles (29 km) wide and attains a depth of" \
                "over a mile (6,093 feet or 1,857 meters).The canyon and adjacent rim are contained" \
                "within Grand Canyon National Park, the Kaibab National Forest, Grand Canyon-Parashant" \
                "National Monument, the Hualapai Indian Reservation, the Havasupai Indian Reservation" \
                "and the Navajo Nation.", country= country6)
session.add(list13)
session.commit()

list12=VisitList(name= "Big Ben", category="national-park", description="It  is a steep-sided" \
                "canyon carved by the Colorado River in Arizona, United States. The Grand Canyon" \
                "is 277 miles (446 km) long, up to 18 miles (29 km) wide and attains a depth of" \
                "over a mile (6,093 feet or 1,857 meters).The canyon and adjacent rim are contained" \
                "within Grand Canyon National Park, the Kaibab National Forest, Grand Canyon-Parashant" \
                "National Monument, the Hualapai Indian Reservation, the Havasupai Indian Reservation" \
                "and the Navajo Nation.", country= country6)
session.add(list12)
session.commit()

list11=VisitList(name= "Buckingham Palace", category="national-park", description="It  is a steep-sided" \
                "canyon carved by the Colorado River in Arizona, United States. The Grand Canyon" \
                "is 277 miles (446 km) long, up to 18 miles (29 km) wide and attains a depth of" \
                "over a mile (6,093 feet or 1,857 meters).The canyon and adjacent rim are contained" \
                "within Grand Canyon National Park, the Kaibab National Forest, Grand Canyon-Parashant" \
                "National Monument, the Hualapai Indian Reservation, the Havasupai Indian Reservation" \
                "and the Navajo Nation.", country= country5)
session.add(list11)
session.commit()






                
