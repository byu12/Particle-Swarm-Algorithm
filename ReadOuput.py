import csv
import ParticleSwarm as ps
import sys


def read_to_csv():
    arguments = ps.parse_arguments(sys.argv[1:])

    print("hahahahhah",arguments)
    with open('C:\\Users\\yubo\\PycharmProjects\\Particle-Swarm-Algorithm\\pso_output.csv', 'w', newline='') as csvFile:
        print("******", csvFile)
        csvwriter = csv.writer(csvFile, delimiter=' ',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csvwriter.writerow(output[0], output[1], output[2], output[3], output[4], output[5], output[6], output[7])

        csvwriter.close()


if __name__ == "__main__":
    read_to_csv()


