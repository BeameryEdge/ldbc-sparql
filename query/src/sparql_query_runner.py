import os
from string import Template
import query_runner

class SparqlQueryRunner(query_runner.QueryRunner):

    short_queries = [
        "",
        "interactive-short-1.sparql",
        "interactive-short-2.sparql",
        "interactive-short-3.sparql",
        "interactive-short-4.sparql",
        "interactive-short-5.sparql",
        "interactive-short-6.sparql",
        "interactive-short-7.sparql",
        "interactive-short-8.sparql",
        "interactive-short-9.sparql"
    ]

    interactive_queries = [
        "",
        "interactive-complex-1.sparql",
        "interactive-complex-2.sparql",
        "interactive-complex-3.sparql",
        "interactive-complex-4.sparql",
        "interactive-complex-5.sparql",
        "interactive-complex-6.sparql",
        "interactive-complex-7.sparql",
        "interactive-complex-8.sparql",
        "interactive-complex-9.sparql",
        "interactive-complex-10.sparql",
        "interactive-complex-11.sparql",
        "interactive-complex-12.sparql",
        "interactive-complex-13.sparql",
        "interactive-complex-14.sparql"
    ]

    def __init__(self, queryPath="queries"):
        query_runner.QueryRunner.__init__(self)
        self.queryPath = queryPath

    def shortQueryImplementation(self):
        return self.short_queries

    def interactiveQueryImplementation(self):
        return self.interactive_queries

    def readQueryFromFile(self, filePath):
        with open(filePath, 'r') as file:
            data = file.read()
            return data

    def duration_days_literal(self, days):
        durationDays = "xsd:duration(\"P" + days + "D\")"
        return durationDays

    def long_literal(self, number):
        return "\"" + number + "\"^^xsd:long"

    def date_literal(self, date):
        if len(date) != 17:
            print('Please set the input date in format: yyyymmddhhmmssmmm')

        year = date[0:4]
        month = date[4:6]
        day = date[6:8]
        hour = date[8:10]
        minute = date[10:12]
        second = date[12:14]
        milli = date[14:17]

        dateTime = "xsd:datetime(\"" + year + "-" + month + "-" + day + "T" + hour + ":" + minute + ":" + second + "." + milli + "Z\")"
        return dateTime

    def string_literal(self, string):
        return "\"" + string + "\""

    def collectionise(self, elements):
        result = "(\"" + "\" \"".join(elements) + "\")"
        return result

    def i_short(self, query_no, personId):
        queryFilePath = os.path.join(self.queryPath, self.short_queries[query_no])
        query = self.readQueryFromFile(queryFilePath)
        qt = Template(query).substitute(personId=self.long_literal(personId))
        return self.runQuery(qt)

    def i_complex_1(self, personId, firstName):
        queryFilePath = os.path.join(self.queryPath, self.interactiveQueryImplementation()[1])
        query = self.readQueryFromFile(queryFilePath)
        qt = Template(query).substitute(personId=self.long_literal(personId), firstName=self.string_literal(firstName))
        return self.runQuery(qt)

    def i_complex_2(self, personId, date):
        dateTime = self.date_literal(date)
        queryFilePath = os.path.join(self.queryPath, self.interactiveQueryImplementation()[2])
        query = self.readQueryFromFile(queryFilePath)
        qt = Template(query).substitute(personId=self.long_literal(personId), maxDate=dateTime)
        return self.runQuery(qt)

    def i_complex_3(self, personId, startDate, days, countryXName, countryYName):
        queryFilePath = os.path.join(self.queryPath, self.interactiveQueryImplementation()[3])
        query = self.readQueryFromFile(queryFilePath)
        qt = Template(query).substitute(
            personId=self.long_literal(personId),
            startDate=self.date_literal(startDate),
            durationDays=self.duration_days_literal(days),
            countryXName=self.string_literal(countryXName),
            countryYName=self.string_literal(countryYName))
        return self.runQuery(qt)

    def i_complex_4(self, personId, startDate, days):
        queryFilePath = os.path.join(self.queryPath, self.interactiveQueryImplementation()[4])
        query = self.readQueryFromFile(queryFilePath)
        qt = Template(query).substitute(
            personId=self.long_literal(personId),
            startDate=self.date_literal(startDate),
            durationDays=self.duration_days_literal(days))
        return self.runQuery(qt)

    def i_complex_5(self, personId, minDate):
        queryFilePath = os.path.join(self.queryPath, self.interactiveQueryImplementation()[5])
        query = self.readQueryFromFile(queryFilePath)
        qt = Template(query).substitute(
            personId=self.long_literal(personId),
            minDate=self.date_literal(minDate))
        return self.runQuery(qt)

    def i_complex_6(self, personId, tagName):
        queryFilePath = os.path.join(self.queryPath, self.interactiveQueryImplementation()[6])
        query = self.readQueryFromFile(queryFilePath)
        qt = Template(query).substitute(
            personId=self.long_literal(personId),
            tagName=self.string_literal(tagName))
        return self.runQuery(qt)

    def i_complex_7(self, personId):
        queryFilePath = os.path.join(self.queryPath, self.interactiveQueryImplementation()[7])
        query = self.readQueryFromFile(queryFilePath)
        qt = Template(query).substitute(
            personId=self.long_literal(personId))
        return self.runQuery(qt)

    def i_complex_8(self, personId):
        queryFilePath = os.path.join(self.queryPath, self.interactiveQueryImplementation()[8])
        query = self.readQueryFromFile(queryFilePath)
        qt = Template(query).substitute(
            personId=self.long_literal(personId))
        return self.runQuery(qt)

    def i_complex_9(self, personId, date):
        queryFilePath = os.path.join(self.queryPath, self.interactiveQueryImplementation()[9])
        query = self.readQueryFromFile(queryFilePath)
        qt = Template(query).substitute(
            personId=self.long_literal(personId),
            maxDate=self.date_literal(date))
        return self.runQuery(qt)

    def i_complex_10(self, personId, month):
        queryFilePath = os.path.join(self.queryPath, self.interactiveQueryImplementation()[10])
        query = self.readQueryFromFile(queryFilePath)
        qt = Template(query).substitute(
            personId=self.long_literal(personId),
            month=month)
        return self.runQuery(qt)

    def i_complex_11(self, personId, country, workFromYear):
        queryFilePath = os.path.join(self.queryPath, self.interactiveQueryImplementation()[11])
        query = self.readQueryFromFile(queryFilePath)
        qt = Template(query).substitute(
            personId=self.long_literal(personId),
            countryName=self.string_literal(country),
            workFromYear=workFromYear)
        return self.runQuery(qt)

    def i_complex_12(self, personId, tagClassName):
        queryFilePath = os.path.join(self.queryPath, self.interactiveQueryImplementation()[12])
        query = self.readQueryFromFile(queryFilePath)
        qt = Template(query).substitute(
            personId=self.long_literal(personId),
            tagClassName=self.string_literal(tagClassName))
        return self.runQuery(qt)

    def i_complex_13(self, person1Id, person2Id):
        queryFilePath = os.path.join(self.queryPath, self.interactiveQueryImplementation()[13])
        query = self.readQueryFromFile(queryFilePath)
        qt = Template(query).substitute(
            person1Id=person1Id,
            person2Id=person2Id)
        return self.runQuery(qt)

    def i_complex_14(self, person1Id, person2Id):
        queryFilePath = os.path.join(self.queryPath, self.interactiveQueryImplementation()[14])
        query = self.readQueryFromFile(queryFilePath)
        qt = Template(query).substitute(
            person1Id=person1Id,
            person2Id=person2Id)
        return self.runQuery(qt)

    def bi_1(self, date):
        queryFilePath = os.path.join(self.queryPath, "bi-1.sparql")
        query = self.readQueryFromFile(queryFilePath)
        qt = Template(query).substitute(
            date=self.date_literal(date)
        )
        return self.runQuery(qt)

    def bi_2(self, startDate, endDate, country1, country2):
        queryFilePath = os.path.join(self.queryPath, "bi-2.sparql")
        query = self.readQueryFromFile(queryFilePath)
        qt = Template(query).substitute(
            startDate=self.date_literal(startDate),
            endDate=self.date_literal(endDate),
            country1=self.string_literal(country1),
            country2=self.string_literal(country2))
        return self.runQuery(qt)

    def bi_3(self, year, month):
        queryFilePath = os.path.join(self.queryPath, "bi-3.sparql")
        query = self.readQueryFromFile(queryFilePath)
        qt = Template(query).substitute(
            year=year,
            month=month)
        return self.runQuery(qt)

    def bi_4(self, tagClass, country):
        queryFilePath = os.path.join(self.queryPath, "bi-4.sparql")
        query = self.readQueryFromFile(queryFilePath)
        qt = Template(query).substitute(
            country=self.string_literal(country),
            tagClass=self.string_literal(tagClass)
        )
        return self.runQuery(qt)

    def bi_5(self, country):
        queryFilePath = os.path.join(self.queryPath, "bi-5.sparql")
        query = self.readQueryFromFile(queryFilePath)
        qt = Template(query).substitute(
            country=self.string_literal(country)
        )
        return self.runQuery(qt)

    def bi_6(self, tag):
        queryFilePath = os.path.join(self.queryPath, "bi-6.sparql")
        query = self.readQueryFromFile(queryFilePath)
        qt = Template(query).substitute(
            tag=self.string_literal(tag)
        )
        return self.runQuery(qt)

    def bi_7(self, tag):
        queryFilePath = os.path.join(self.queryPath, "bi-7.sparql")
        query = self.readQueryFromFile(queryFilePath)
        qt = Template(query).substitute(
            tag=self.string_literal(tag)
        )
        return self.runQuery(qt)

    def bi_8(self, tag):
        queryFilePath = os.path.join(self.queryPath, "bi-8.sparql")
        query = self.readQueryFromFile(queryFilePath)
        qt = Template(query).substitute(
            tag=self.string_literal(tag)
        )
        return self.runQuery(qt)

    def bi_9(self, tagClass1, tagClass2, threshold):
        queryFilePath = os.path.join(self.queryPath, "bi-9.sparql")
        query = self.readQueryFromFile(queryFilePath)
        qt = Template(query).substitute(
            tagClass1=self.string_literal(tagClass1),
            tagClass2=self.string_literal(tagClass2),
            threshold=threshold
        )
        return self.runQuery(qt)

    def bi_10(self, tag, date):
        queryFilePath = os.path.join(self.queryPath, "bi-10.sparql")
        query = self.readQueryFromFile(queryFilePath)
        qt = Template(query).substitute(
            date=self.date_literal(date),
            tag=self.string_literal(tag)
        )
        return self.runQuery(qt)

    def bi_11(self, country, blocklist):
        queryFilePath = os.path.join(self.queryPath, "bi-11.sparql")
        query = self.readQueryFromFile(queryFilePath)
        qt = Template(query).substitute(
            blacklist="\"" + "| ".join(blocklist) + "\"",
            country=self.string_literal(country)
        )
        return self.runQuery(qt)

    def bi_12(self, date, likeThreshold): 
        queryFilePath = os.path.join(self.queryPath, "bi-12.sparql")
        query = self.readQueryFromFile(queryFilePath)
        qt = Template(query).substitute(
            date=self.date_literal(date),
            likeThreshold=likeThreshold
        )
        return self.runQuery(qt)

    def bi_13(self, country):
        queryFilePath = os.path.join(self.queryPath, "bi-13.sparql")
        query = self.readQueryFromFile(queryFilePath)
        qt = Template(query).substitute(
            country=self.string_literal(country)
        )
        return self.runQuery(qt)

    def bi_14(self, startDate, endDate):
        queryFilePath = os.path.join(self.queryPath, "bi-14.sparql")
        query = self.readQueryFromFile(queryFilePath)
        qt = Template(query).substitute(
            startDate=self.date_literal(startDate),
            endDate=self.date_literal(endDate)
        )
        return self.runQuery(qt)

    def bi_15(self, country):
        queryFilePath = os.path.join(self.queryPath, "bi-15.sparql")
        query = self.readQueryFromFile(queryFilePath)
        qt = Template(query).substitute(
            country=self.string_literal(country)
        )
        return self.runQuery(qt)

    def bi_16(self, personId, country, tagClass, minPathDistance, maxPathDistance):
        queryFilePath = os.path.join(self.queryPath, "bi-16.sparql")
        query = self.readQueryFromFile(queryFilePath)
        qt = Template(query).substitute(
            personId=self.long_literal(personId),
            country=self.string_literal(country),
            minPathDistance=minPathDistance,
            maxPathDistance=maxPathDistance,
            tagClass=self.string_literal(tagClass)
        )
        return self.runQuery(qt)

    def bi_17(self, country):
        queryFilePath = os.path.join(self.queryPath, "bi-17.sparql")
        query = self.readQueryFromFile(queryFilePath)
        qt = Template(query).substitute(
            country=self.string_literal(country)
        )
        return self.runQuery(qt)

    def bi_18(self, date, lengthThreshold, languages):
        queryFilePath = os.path.join(self.queryPath, "bi-18.sparql")
        query = self.readQueryFromFile(queryFilePath)
        qt = Template(query).substitute(
            date=self.date_literal(date),
            languages=self.collectionise(languages),
            lengthThreshold=lengthThreshold
        )
        return self.runQuery(qt)

    def bi_19(self, date, tagClass1, tagClass2):
        queryFilePath = os.path.join(self.queryPath, "bi-19.sparql")
        query = self.readQueryFromFile(queryFilePath)
        qt = Template(query).substitute(
            date=date,
            tagClass1=self.string_literal(tagClass1),
            tagClass2=self.string_literal(tagClass2)
        )
        return self.runQuery(qt)

    def bi_20(self, tagClasses):
        queryFilePath = os.path.join(self.queryPath, "bi-20.sparql")
        query = self.readQueryFromFile(queryFilePath)
        qt = Template(query).substitute(
            tagClasses=self.collectionise(tagClasses)
        )
        return self.runQuery(qt)

    def bi_21(self, country, endDate):
        queryFilePath = os.path.join(self.queryPath, "bi-21.sparql")
        query = self.readQueryFromFile(queryFilePath)
        qt = Template(query).substitute(
            country=self.string_literal(country),
            endDate=self.date_literal(endDate)
        )
        return self.runQuery(qt)

    def bi_22(self, country1, country2):
        queryFilePath = os.path.join(self.queryPath, "bi-22.sparql")
        query = self.readQueryFromFile(queryFilePath)
        qt = Template(query).substitute(
            country1=self.string_literal(country1),
            country2=self.string_literal(country2)
        )
        return self.runQuery(qt)

    def bi_23(self, country):
        queryFilePath = os.path.join(self.queryPath, "bi-23.sparql")
        query = self.readQueryFromFile(queryFilePath)
        qt = Template(query).substitute(
            country=self.string_literal(country)
        )
        return self.runQuery(qt)

    def bi_24(self, tagClass):
        queryFilePath = os.path.join(self.queryPath, "bi-24.sparql")
        query = self.readQueryFromFile(queryFilePath)
        qt = Template(query).substitute(
            tagClass=self.string_literal(tagClass)
        )
        return self.runQuery(qt)

    def bi_25(self, person1Id, person2Id, startDate, endDate):
        pass
