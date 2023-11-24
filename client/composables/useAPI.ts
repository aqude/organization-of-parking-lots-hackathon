type ArgumentTypes<F extends Function> = F extends (...args: infer A) => any ? A : never;

export const useAPI = (request: ArgumentTypes<typeof useFetch>[0], opts: ArgumentTypes<typeof useFetch>[1]) => {
	return useFetch(`http://localhost:8000${request}`, opts)
}