import EbayGetCategories
import Create_database
import Create_HTML
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--rebuild",action="store_true"
                    ,help="Store categories in database")
parser.add_argument("--render",
                    help="Create HTML file")
args = parser.parse_args()

if args.rebuild:
    EbayGetCategories()
    create_database()
elif args.render:
    create_HTML(args.render)
