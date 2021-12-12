from utils.utils import file_to_collection
from collections import defaultdict


class PassagePathing:

    def __init__(self, input_file):
        self.adj_list = self._create_adjacency_list(file_to_collection(input_file))
        pass

    def _create_adjacency_list(self, data):
        adj_list = defaultdict(list)
        for edge in data:
            source, destination = edge.split('-')
            if destination not in ['start']:
                adj_list[source].append(destination)
            if destination not in ['end'] and source not in ['start']:
                adj_list[destination].append(source)
        return adj_list

    def _find_paths(self, source, destination, twice):
        result = []
        visited = set()
        self._dfs(source, destination, [], result, visited, twice)
        return result

    def _dfs(self, source, final_destination, current_path, result, visited, twice):
        if source == final_destination:
            current_path.append(source)
            result.append(','.join(current_path))
            current_path.pop()
            return
        if source not in visited or source.isupper() or twice:
            current_path.append(source)
            temp_twice = twice
            if not source.isupper():
                if temp_twice and source in visited:
                    temp_twice = False
                visited.add(source)
            for destination in self.adj_list[source]:
                self._dfs(destination, final_destination, current_path, result, visited, temp_twice)
            current_path.pop()
            if not source.isupper() and ((twice and temp_twice) or (not twice and not temp_twice)):
                visited.remove(source)

    def part1(self):
        return len(self._find_paths('start', 'end', False))

    def part2(self):
        return len(self._find_paths('start', 'end', True))
