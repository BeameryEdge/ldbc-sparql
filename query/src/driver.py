import json
import os, logging
from datetime import datetime as dt
from timeit import default_timer as timer
import query_runner

def run_query_is(seed, query_num, runner):
    if query_num in range(1, 10):
        return runner.i_short(query_num, seed.get("personId"))
    else:
        print("Invalid query: " + str(query_num))

def run_query_ic(seed, query_num, runner):
    if query_num == 1:
        return runner.i_complex_1(seed.get("personId"), seed.get("firstName"))
    elif query_num == 2:
        return runner.i_complex_2(seed.get("personId"), seed.get("maxDate"))
    elif query_num == 3:
        return runner.i_complex_3(seed.get("personId"), seed.get("startDate"), seed.get("durationDays"),
                                  seed.get("countryXName"), seed.get("countryYName"))
    elif query_num == 4:
        return runner.i_complex_4(seed.get("personId"), seed.get("startDate"), seed.get("durationDays"))
    elif query_num == 5:
        return runner.i_complex_5(seed.get("personId"), seed.get("minDate"))
    elif query_num == 6:
        return runner.i_complex_6(seed.get("personId"), seed.get("tagName"))
    elif query_num == 7:
        return runner.i_complex_7(seed.get("personId"))
    elif query_num == 8:
        return runner.i_complex_8(seed.get("personId"))
    elif query_num == 9:
        return runner.i_complex_9(seed.get("personId"), seed.get("maxDate"))
    elif query_num == 10:
        return runner.i_complex_10(seed.get("personId"), seed.get("month"))
    elif query_num == 11:
        return runner.i_complex_11(seed.get("personId"), seed.get("countryName"), seed.get("workFromYear"))
    elif query_num == 12:
        return runner.i_complex_12(seed.get("personId"), seed.get("tagClassName"))
    elif query_num == 13:
        return runner.i_complex_13(seed.get("person1Id"), seed.get("person2Id"))
    elif query_num == 14:
        return runner.i_complex_14(seed.get("person1Id"), seed.get("person2Id"))
    else:
        print("Invalid query: " + str(query_num))


def run_query_bi(seed, query_num, runner):
    if query_num == 1:
        return runner.bi_1(seed.get("maxDate"))
    elif query_num == 2:
        return runner.bi_2(seed.get("startDate"), seed.get("endDate"), seed.get("country1Name"),
                           seed.get("country2Name"))
    elif query_num == 3:
        return runner.bi_3(seed.get("year1"), seed.get("month1"))
    elif query_num == 4:
        return runner.bi_4(seed.get("tagClassName"), seed.get("countryName"))
    elif query_num == 5:
        return runner.bi_5(seed.get("countryName"))
    elif query_num == 6:
        return runner.bi_6(seed.get("tagName"))
    elif query_num == 7:
        return runner.bi_7(seed.get("tagName"))
    elif query_num == 8:
        return runner.bi_8(seed.get("tagName"))
    elif query_num == 9:
        return runner.bi_9(seed.get("tagClass1Name"), seed.get("tagClass2Name"), seed.get("threshold"))
    elif query_num == 10:
        return runner.bi_10(seed.get("tagName"), seed.get("minDate"))
    elif query_num == 11:
        return runner.bi_11(seed.get("countryName"), seed.get("blacklist"))
    elif query_num == 12:
        return runner.bi_12(seed.get("minDate"), seed.get("likeThreshold"))
    elif query_num == 13:
        return runner.bi_13(seed.get("countryName"))
    elif query_num == 14:
        return runner.bi_14(seed.get("startDate"), seed.get("endDate"))
    elif query_num == 15:
        return runner.bi_15(seed.get("countryName"))
    elif query_num == 16:
        return runner.bi_16(seed.get("personId"), seed.get("countryName"), seed.get("tagClassName"),
                            seed.get("minPathDistance"), seed.get("maxPathDistance"))
    elif query_num == 17:
        return runner.bi_17(seed.get("countryName"))
    elif query_num == 18:
        return runner.bi_18(seed.get("minDate"), seed.get("lengthThreshold"), seed.get("languages"))
    elif query_num == 19:
        return runner.bi_19(seed.get("minDate"), seed.get("tagClass1Name"), seed.get("tagClass2Name"))
    elif query_num == 20:
        return runner.bi_20(seed.get("tagClassNames"))
    elif query_num == 21:
        return runner.bi_21(seed.get("countryName"), seed.get("endDate"))
    elif query_num == 22:
        return runner.bi_22(seed.get("country1Name"), seed.get("country2Name"))
    elif query_num == 23:
        return runner.bi_23(seed.get("countryName"))
    elif query_num == 24:
        return runner.bi_24(seed.get("tagClassName"))
    elif query_num == 25:
        return runner.bi_25(seed.get("person1Id"), seed.get("person2Id"), seed.get("startDate"), seed.get("endDate"), )
    else:
        print("Invalid query: " + str(query_num))


def run_query(seed, query_type, query_num, runner):
    if query_type == "ic":
        return run_query_ic(seed, query_num, runner)
    elif query_type == "bi":
        return run_query_bi(seed, query_num, runner)
    elif query_type == "is":
        return run_query_is(seed, query_num, runner)
    else:
        print("Invalid query: " + str(query_num))

def log_query(query, backend, database, query_type, query_num, seed):
    resultPath = "query/"
    if not os.path.exists(os.path.dirname(resultPath)):
        try:
            os.makedirs(os.path.dirname(resultPath))
        except OSError as exc:
            if exc.errno != errno.EEXIST:
                raise

    query_file = backend + "-" + database + "-" + query_type + str(query_num) + "-" + str(seed) + ".sparql"
    ofile = open(resultPath + query_file, 'w')
    ofile.write(query)
    ofile.close()

def run_queries(seeds, query_type, query_num, runner: query_runner):
    # create result folder
    resultPath = "result/"
    if not os.path.exists(os.path.dirname(resultPath)):
        try:
            os.makedirs(os.path.dirname(resultPath))
        except OSError as exc:
            if exc.errno != errno.EEXIST:
                raise

    query = query_type + str(query_num)
    ofile = open(resultPath + query, 'w')

    total_time = 0.0
    report = "\n---------- " + str(dt.now()) + "  " + "  ----------\n"
    print(report)

    seed_count = 1
    for seed in seeds:
        start = timer()

        query_string, results = run_query(seed, query_type, query_num, runner)
        #if logging.root.isEnabledFor(getattr(logging, 'DEBUG')):
        log_query(query_string, runner.backendName(), runner.database, query_type, query_num, seed_count)
        seed_count += 1

        end = timer()
        exe_time = end - start
        total_time += exe_time

        line = query + ": " + json.dumps(seed) + "," + str(exe_time) + " seconds"
        print(line)
        ofile.write(line + "\n")

    summary = "summary," + query + "," + str(total_time / len(seeds)) + " seconds"
    ofile.write(summary)
    print(summary)
    ofile.close()
