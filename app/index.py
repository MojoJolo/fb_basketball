from flask import request, jsonify, render_template, redirect, url_for
from app import app

from ga import GA

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ga')
def computeGA():
    gen_algo = GA()

    # min = -2.24
    # max = -0.76
    min = -2.5
    max = 0
    population_count = 20

    currX = float(request.args.get('currX', 187.5))
    currY = float(request.args.get('currY', 530))

    targetX = float(request.args.get('targetX', 187.5))
    targetY = 0

    if targetX > currX:
        targetX = sum([targetX, currX]) / 2
    elif targetX < currX:
        targetX = sum([targetX, currX]) / 2

    current_point = {
        'x': currX,
        'y': currY
    }
    target_point = {
        'x': targetX,
        'y': targetY
    }

    popul = gen_algo.population(population_count, min, max)

    generations = [popul]
    generation_count = 10

    for i in xrange(generation_count):
        popul = gen_algo.evolve(min, max, popul, current_point, target_point)
        generations.append(popul)

    best_indiv = [(gen_algo.fitness(current_point, target_point, indiv), indiv) for indiv in generations[-1]]
    best_indiv = [x[1] for x in sorted(best_indiv)][0]

    return jsonify({'angle': best_indiv})