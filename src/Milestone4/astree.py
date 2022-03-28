from parser import buildAndCompile
import sys

ast = buildAndCompile()
path_to_source_file = sys.argv[1][:-3]
node_ids = [f'\t0 [label={ast}];']
print(f"Saving to {path_to_source_file}.dot ...")
with open(f"{path_to_source_file}.dot", 'w') as f:
    f.write("digraph G {\n")
    def dfs(node, id):
        global node_ids
        if hasattr(node, 'children') and node.children is not None:
            for c in node.children:
                node_ids.append(f'\t{len(node_ids)} [label="{c}"];')
                f.write(f'\t{id} -> {len(node_ids)-1};\n')
                dfs(c, len(node_ids)-1)

    dfs(ast,0)
    f.writelines(node_ids)

    f.write("\n}")