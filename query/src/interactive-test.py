import unittest

import driver
import seed_generator
import stardog_query_runner
import virtuoso_query_runner
import query_runner
import sys, logging

SFACTOR = "sf01"
PATH_TO_SEEDS = 
DATE_FORMAT = "%Y%m%d%H%M%S000"
TIMEOUT = 2
NO_OF_SEEDS = 1
QUERY_DIR = "../sparql"

class TestInteractive(unittest.TestCase):

    def testInteractiveShortStardog(self):
        stardogRunner = stardog_query_runner.StardogQueryRunner(SFACTOR, TIMEOUT, QUERY_DIR)
        self.executeWithBackend(stardogRunner, "is", 1, 7)

    def testInteractiveShortVirtuoso(self):
        virtuosoRunner = virtuoso_query_runner.VirtuosoQueryRunner("http://www.ldbc.eu/" + SFACTOR, TIMEOUT, QUERY_DIR)
        self.executeWithBackend(virtuosoRunner, "is", 1, 7)

    def testInteractiveComplexStardog(self):
        stardogRunner = stardog_query_runner.StardogQueryRunner(SFACTOR, TIMEOUT, QUERY_DIR)
        self.executeWithBackend(stardogRunner, "ic", 1, 12)

    def testInteractiveComplexVirtuoso(self):
        virtuosoRunner = virtuoso_query_runner.VirtuosoQueryRunner("http://www.ldbc.eu/" + SFACTOR, TIMEOUT, QUERY_DIR)
        self.executeWithBackend(virtuosoRunner, "ic", 1, 12)
    
    @unittest.skip
    def testInteractiveCrossImplementation(self, runner: query_runner, another_runner: query_runner, ):
        query_type = "ic"
        virtuosoRunner = virtuoso_query_runner.VirtuosoQueryRunner("http://www.ldbc.eu/" + SFACTOR, TIMEOUT, QUERY_DIR)
        stardogRunner = stardog_query_runner.StardogQueryRunner(SFACTOR, TIMEOUT, QUERY_DIR)
        self.crossExecute(virtuosoRunner, stardogRunner, query_type, 1, 13)

    def executeWithBackend(self, runner: query_runner, query_type, startQ, endQ):
        logging.basicConfig(stream=sys.stdout, level='INFO', format="%(message)s")

        for qno in range(startQ, endQ + 1):
            print( runner.backendName() + ":Interactive Complex " + str(qno))
            seeds = seed_generator.get_seeds(PATH_TO_SEEDS, NO_OF_SEEDS, query_type, qno, DATE_FORMAT)
            query_ok = True
            for seed_no in range(0, len(seeds)):
                seed = seeds[seed_no]
                results = driver.run_query(seed, query_type, qno, runner)
                if results == None or len(results) == 0:
                    query_ok = False
            self.assertTrue(query_ok) 
            
    def crossExecute(self, runner: query_runner, another_runner: query_runner, query_type, startQ, endQ):
        for qno in range(startQ, endQ + 1):
            print("Interactive Complex " + str(qno))
            seeds = seed_generator.get_seeds(PATH_TO_SEEDS, NO_OF_SEEDS, query_type, qno, DATE_FORMAT)
            query_ok = False
            for seed_no in range(0, len(seeds)):
                seed = seeds[seed_no]
                results = driver.run_query(seed, query_type, qno, runner)
                anotherResults = driver.run_query(seed, query_type, qno, another_runner)

                if results != None and anotherResults != None:
                    print("v: " + str(len(results)) + " s: " + str(len(anotherResults)))
                    self.assertEqual(len(results), len(anotherResults))
                    query_ok = True
            self.assertTrue(query_ok)


if __name__ == '__main__':
    unittest.main()
