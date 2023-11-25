type ArgumentTypes<F extends Function> = F extends (...args: infer A) => any ? A : never;

export const useAPI = async (request: ArgumentTypes<typeof useFetch>[0], opts?: ArgumentTypes<typeof useFetch>[1] & { headers?: Record<string, string> }, body_process?: boolean) => {
	const customHeaders = {
		"Content-Type": "application/x-www-form-urlencoded",
	};

	const mergedOpts = {
		...opts,
		body: opts ? (body_process ? new URLSearchParams(Object.entries(opts.body as any)).toString() : opts.body) : undefined,
		headers: opts ? (body_process ? { ...opts.headers, ...customHeaders } : undefined) : undefined,
	};

	return await useFetch(`http://localhost${request}`, mergedOpts ? mergedOpts : undefined);
};