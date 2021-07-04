import subprocess

OUTPUT_FLAG = 'OpenSourceOutputFlag'

systems = [
    # 'ready_model', 
    'pipeswitch', 
    # 'mps', 
    # 'stop_and_start'
]

models = [
    'resnet152',
    # 'inception_v3',
    # 'bert_base',
]

def main():
    data = {}
    for system in systems:
        for model in models:
            # Run the experiment
            result = subprocess.run(['bash', 'scripts/figures/figure5/figure5_%s_%s/host_run_data.sh' % (system, model)])

            # Get output
            output = result.stdout.decode('utf-8')
            lines = output.split('\n')
            for line in lines:
                line = line.strip()
                if OUTPUT_FLAG in line:
                    parts = line.split(',')
                    latency = float(parts[0].strip())
                    stdev = float(parts[1].strip())
                    count = int(parts[2])
                    data[(system, model)] = latency
                    break
    print (data)

    # Plot the figure

if __name__ == '__main__':
    main()