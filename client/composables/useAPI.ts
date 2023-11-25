type ArgumentTypes<F extends Function> = F extends (...args: infer A) => any ? A : never;

export const useAPI = (request: ArgumentTypes<typeof useFetch>[0], opts: ArgumentTypes<typeof useFetch>[1] & { headers?: Record<string, string> }) => {
	const customHeaders = {
		"Content-Type": "application/x-www-form-urlencoded",
	};

	const mergedOpts = {
		...opts,
		headers: { ...opts.headers, ...customHeaders },
	};

	return useFetch(`http://localhost:80${request}`, mergedOpts);
};