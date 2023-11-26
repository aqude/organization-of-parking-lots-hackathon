type ArgumentTypes<F extends Function> = F extends (...args: infer A) => any ? A : never;

export const useAPI = async (request: ArgumentTypes<typeof useFetch>[0], opts?: ArgumentTypes<typeof useFetch>[1] & { headers?: Record<string, string> }, body_process?: boolean) => {
	const customHeaders = body_process ? {
		"Content-Type": "application/x-www-form-urlencoded",
	} : undefined;

	const mergedOpts = {
		...opts,
		body: opts ? (body_process ? new URLSearchParams(Object.entries(opts.body as any)).toString() : opts.body) : undefined,
		headers: opts ? { ...opts.headers, ...customHeaders } : undefined,
	};
	console.log(mergedOpts)
	return await useFetch(`http://localhost${request}`, mergedOpts ? mergedOpts : undefined);
};