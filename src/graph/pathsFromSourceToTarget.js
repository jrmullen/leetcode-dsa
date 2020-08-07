'use strict';

/**
 * @param {number[][]} graph
 * @return {number[][]}
 */
const allPathsSourceTarget = (graph) => {
    const result = [];
    const queue = [];

    // Start at node 0
    queue.push([0]);

    const goalNode = graph.length - 1;

    while (queue.length !== 0) {
        const path = queue.shift();

        const lastNode = path[path.length - 1];

        // if the last node of the path is the goal node, we've successfully found a path
        if (lastNode === goalNode) {
            result.push(path);
        } else {
            // Update the path to include its neighbors
            const neighbors = graph[lastNode];
            for (const neighbor of neighbors) {

                // Copy path
                const newPath = [...path];

                // Add the neighbors to the path & push to the queue
                newPath.push(neighbor);
                queue.push(newPath);
            }
        }
    }

    return result;
};

const input = [[1,2],[3],[3],[]];

console.log(allPathsSourceTarget(input));
