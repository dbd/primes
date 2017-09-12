#!/usr/bin/python
#r=10000
#s=140963029527114894353632157291756673901899008181658496374746593169292421668039669963902715676190525233646178874981391895397601325181517275902314362944325352415310030571649856840054458940146187031029826636128819133607109261046933427124098540381017025394756742354324296564267176458779256586360429089589888159961278883685216141576655482836407684515873590169023479892241887659138275492777595656896741648160917993581002652836744695240387293782480827506825396621016066132740733828096395850409360813771252333678060040654330353801279283884938926681398203950021119857360438617753586097094753592118449706093895724955206821203922462723707935034434870322812162234111223067006552282337095232009616974104056207192419407667994658198522691011050665891764196271782695145463362828886382496525052594594015660477823252284907445245560518490008091467892269721412904418956516004587101839615674549405494758651620844853888300023135140173371260341132550275168365856244074476795277557330280884129662740039374757499857847308470209024394825584381962253153551
#s=0

from nzmath import prime
from pprint import pprint
import argparse

parser = argparse.ArgumentParser(description='Find some primes or somethings')
parser.add_argument('--range','-r', type=int,
                    help='size of range to test')
parser.add_argument('--start','-s', type=int,
                    help='starting value to test')

args = parser.parse_args()

primes = []

for i in range(args.start,args.start+args.range):
    primed = prime.bigprimeq(i)
    if primed:
        primes.append("Is prime:"+str(i**3-((i-1)**3)))

#pprint(primes)
total_primes = len(primes)
#print("Total primes found:"+str(total_primes))
#print("Total samples not prime:"+str(args.range-(len(primes))))
ratio = float(total_primes)/args.range
#print("Ratio of primes to not:"+str(ratio))
print(str(args.range) + ":" + str(ratio))
