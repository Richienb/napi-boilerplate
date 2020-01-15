#define NAPI_VERSION 4
#include <napi.h>

using namespace Napi;

Value helloWorld(const CallbackInfo& info) {
	Env env = info.Env();

	return String::New(env, "Hello World!");
}

Object Init(Env env, Object exports) {
	exports.Set(String::New(env, "helloWorld"), Function::New(env, helloWorld));
	return exports;
}

NODE_API_MODULE(NODE_GYP_MODULE_NAME, Init)
