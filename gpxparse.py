import gpxpy 
import gpxpy.gpx 
import datetime as dt
import argparse
import sys
import subprocess

de main():
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument('input', help='Relative or absolute path of the input GPX file')#, nargs='*')
    parser.add_argument('-o', '--output', default='waypoint.csv', help='Relative or absolute path of the output PDF file, (default: merge_file.pdf)')
    parser.add_argument('--open', action='store_true', default=False,
                            help='Open  text file after ')
    args = parser.parse_args()
    print(args.input)

    if args.input:
        
        outputFile = open(args.output, 'w')
        gpx_file = open(args.input, 'r') 
        gpx = gpxpy.parse(gpx_file)
        for waypoint in gpx.waypoints:
            print('{0};{1};{2};{3};{4}'.format(waypoint.name, waypoint.latitude, waypoint.longitude, dt.datetime.fromisoformat(str(waypoint.time)).strftime("%d.%m.%y %H:%M"), waypoint.description if waypoint.description != None else "" ), file=outputFile)
        outputFile.close()
    else:
        print("Du må skrive inne en gpx-fil")

    if args.open:
        if sys.platform == "win32":
            subprocess.call(["explorer.exe", args.output])
        else:
            subprocess.call(["evince", args.output])

#   for track in gpx.tracks:
#        for segment in track.segments:
#            for point in segment.points:
#                print('Point at ({0},{1}) -> {2}'.format(point.latitude, point.longitude, point.elevation))
#          for route in gpx.routes:
#        print('Route:')



if __name__ == "__main__": 
	# calling the main function 
	main()
