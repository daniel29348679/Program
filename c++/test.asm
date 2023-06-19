	.file	"test.cpp"
	.text
	.p2align 4
	.def	__tcf_0;	.scl	3;	.type	32;	.endef
	.seh_proc	__tcf_0
__tcf_0:
.LFB11991:
	.seh_endprologue
	leaq	_ZStL8__ioinit(%rip), %rcx
	jmp	_ZNSt8ios_base4InitD1Ev
	.seh_endproc
	.align 2
	.p2align 4
	.def	_ZNSt8_Rb_treeIxSt4pairIKxiESt10_Select1stIS2_ESt4lessIxESaIS2_EE8_M_eraseEPSt13_Rb_tree_nodeIS2_E.isra.0;	.scl	3;	.type	32;	.endef
	.seh_proc	_ZNSt8_Rb_treeIxSt4pairIKxiESt10_Select1stIS2_ESt4lessIxESaIS2_EE8_M_eraseEPSt13_Rb_tree_nodeIS2_E.isra.0
_ZNSt8_Rb_treeIxSt4pairIKxiESt10_Select1stIS2_ESt4lessIxESaIS2_EE8_M_eraseEPSt13_Rb_tree_nodeIS2_E.isra.0:
.LFB12015:
	pushq	%r15
	.seh_pushreg	%r15
	pushq	%r14
	.seh_pushreg	%r14
	pushq	%r13
	.seh_pushreg	%r13
	pushq	%r12
	.seh_pushreg	%r12
	pushq	%rbp
	.seh_pushreg	%rbp
	pushq	%rdi
	.seh_pushreg	%rdi
	pushq	%rsi
	.seh_pushreg	%rsi
	pushq	%rbx
	.seh_pushreg	%rbx
	subq	$40, %rsp
	.seh_stackalloc	40
	.seh_endprologue
	movq	%rcx, 112(%rsp)
	testq	%rcx, %rcx
	je	.L3
.L21:
	movq	112(%rsp), %rax
	movq	24(%rax), %r13
	testq	%r13, %r13
	je	.L5
.L20:
	movq	24(%r13), %r14
	testq	%r14, %r14
	je	.L6
.L19:
	movq	24(%r14), %r15
	testq	%r15, %r15
	je	.L7
.L18:
	movq	24(%r15), %rbx
	testq	%rbx, %rbx
	je	.L8
.L17:
	movq	24(%rbx), %rsi
	testq	%rsi, %rsi
	je	.L9
.L16:
	movq	24(%rsi), %rbp
	testq	%rbp, %rbp
	je	.L10
.L15:
	movq	24(%rbp), %rdi
	testq	%rdi, %rdi
	je	.L11
.L14:
	movq	24(%rdi), %r12
	testq	%r12, %r12
	je	.L12
.L13:
	movq	24(%r12), %rcx
	call	_ZNSt8_Rb_treeIxSt4pairIKxiESt10_Select1stIS2_ESt4lessIxESaIS2_EE8_M_eraseEPSt13_Rb_tree_nodeIS2_E.isra.0
	movq	%r12, %rcx
	movq	16(%r12), %r12
	movl	$48, %edx
	call	_ZdlPvy
	testq	%r12, %r12
	jne	.L13
.L12:
	movq	16(%rdi), %r12
	movl	$48, %edx
	movq	%rdi, %rcx
	call	_ZdlPvy
	testq	%r12, %r12
	je	.L11
	movq	%r12, %rdi
	jmp	.L14
.L9:
	movq	16(%rbx), %rsi
	movl	$48, %edx
	movq	%rbx, %rcx
	call	_ZdlPvy
	testq	%rsi, %rsi
	je	.L8
	movq	%rsi, %rbx
	jmp	.L17
	.p2align 4,,10
	.p2align 3
.L10:
	movq	16(%rsi), %rdi
	movl	$48, %edx
	movq	%rsi, %rcx
	call	_ZdlPvy
	testq	%rdi, %rdi
	je	.L9
	movq	%rdi, %rsi
	jmp	.L16
.L8:
	movq	16(%r15), %rbx
	movl	$48, %edx
	movq	%r15, %rcx
	call	_ZdlPvy
	testq	%rbx, %rbx
	je	.L7
	movq	%rbx, %r15
	jmp	.L18
	.p2align 4,,10
	.p2align 3
.L11:
	movq	16(%rbp), %rdi
	movl	$48, %edx
	movq	%rbp, %rcx
	call	_ZdlPvy
	testq	%rdi, %rdi
	je	.L10
	movq	%rdi, %rbp
	jmp	.L15
.L7:
	movq	16(%r14), %rbx
	movl	$48, %edx
	movq	%r14, %rcx
	call	_ZdlPvy
	testq	%rbx, %rbx
	je	.L6
	movq	%rbx, %r14
	jmp	.L19
.L6:
	movq	16(%r13), %rbx
	movl	$48, %edx
	movq	%r13, %rcx
	call	_ZdlPvy
	testq	%rbx, %rbx
	je	.L5
	movq	%rbx, %r13
	jmp	.L20
.L5:
	movq	112(%rsp), %rax
	movl	$48, %edx
	movq	16(%rax), %rbx
	movq	%rax, %rcx
	call	_ZdlPvy
	testq	%rbx, %rbx
	je	.L3
	movq	%rbx, 112(%rsp)
	jmp	.L21
.L3:
	addq	$40, %rsp
	popq	%rbx
	popq	%rsi
	popq	%rdi
	popq	%rbp
	popq	%r12
	popq	%r13
	popq	%r14
	popq	%r15
	ret
	.seh_endproc
	.align 2
	.p2align 4
	.def	_ZNSt8_Rb_treeIxSt4pairIKxiESt10_Select1stIS2_ESt4lessIxESaIS2_EE22_M_emplace_hint_uniqueIJRKSt21piecewise_construct_tSt5tupleIJRS1_EESD_IJEEEEESt17_Rb_tree_iteratorIS2_ESt23_Rb_tree_const_iteratorIS2_EDpOT_.isra.0;	.scl	3;	.type	32;	.endef
	.seh_proc	_ZNSt8_Rb_treeIxSt4pairIKxiESt10_Select1stIS2_ESt4lessIxESaIS2_EE22_M_emplace_hint_uniqueIJRKSt21piecewise_construct_tSt5tupleIJRS1_EESD_IJEEEEESt17_Rb_tree_iteratorIS2_ESt23_Rb_tree_const_iteratorIS2_EDpOT_.isra.0
_ZNSt8_Rb_treeIxSt4pairIKxiESt10_Select1stIS2_ESt4lessIxESaIS2_EE22_M_emplace_hint_uniqueIJRKSt21piecewise_construct_tSt5tupleIJRS1_EESD_IJEEEEESt17_Rb_tree_iteratorIS2_ESt23_Rb_tree_const_iteratorIS2_EDpOT_.isra.0:
.LFB12017:
	pushq	%r14
	.seh_pushreg	%r14
	pushq	%r13
	.seh_pushreg	%r13
	pushq	%r12
	.seh_pushreg	%r12
	pushq	%rbp
	.seh_pushreg	%rbp
	pushq	%rdi
	.seh_pushreg	%rdi
	pushq	%rsi
	.seh_pushreg	%rsi
	pushq	%rbx
	.seh_pushreg	%rbx
	subq	$32, %rsp
	.seh_stackalloc	32
	.seh_endprologue
	movq	%rcx, %r12
	movl	$48, %ecx
	movq	%r8, %rbx
	movq	%rdx, %r13
	call	_Znwy
	leaq	8(%r12), %r14
	movq	%rax, %rbp
	movq	(%rbx), %rax
	movq	%r13, %rbx
	movl	$0, 40(%rbp)
	movq	(%rax), %rdi
	movq	%rdi, 32(%rbp)
	cmpq	%r13, %r14
	je	.L114
	movq	32(%r13), %rsi
	cmpq	%rsi, %rdi
	jge	.L70
	movq	24(%r12), %rsi
	cmpq	%r13, %rsi
	je	.L67
	movq	%r13, %rcx
	call	_ZSt18_Rb_tree_decrementPSt18_Rb_tree_node_base
	cmpq	32(%rax), %rdi
	jg	.L115
	movq	16(%r12), %rbx
	testq	%rbx, %rbx
	jne	.L77
	jmp	.L116
	.p2align 4,,10
	.p2align 3
.L101:
	movq	%rax, %rbx
.L77:
	movq	32(%rbx), %rdx
	movq	24(%rbx), %rax
	cmpq	%rdx, %rdi
	cmovl	16(%rbx), %rax
	setl	%cl
	testq	%rax, %rax
	jne	.L101
	movq	%rbx, %r8
	testb	%cl, %cl
	jne	.L75
.L78:
	cmpq	%rdx, %rdi
	jg	.L112
	.p2align 4,,10
	.p2align 3
.L69:
	movl	$48, %edx
	movq	%rbp, %rcx
	call	_ZdlPvy
.L111:
	movq	%rbx, %rax
	addq	$32, %rsp
	popq	%rbx
	popq	%rsi
	popq	%rdi
	popq	%rbp
	popq	%r12
	popq	%r13
	popq	%r14
	ret
	.p2align 4,,10
	.p2align 3
.L70:
	jle	.L69
	cmpq	32(%r12), %r13
	je	.L113
	movq	%r13, %rcx
	call	_ZSt18_Rb_tree_incrementPSt18_Rb_tree_node_base
	cmpq	32(%rax), %rdi
	jge	.L83
	cmpq	$0, 24(%r13)
	je	.L85
	movq	%rax, %rbx
	movl	$1, %ecx
	jmp	.L86
	.p2align 4,,10
	.p2align 3
.L105:
	movq	%rax, %rbx
.L89:
	movq	32(%rbx), %rdx
	movq	24(%rbx), %rax
	cmpq	%rdx, %rdi
	cmovl	16(%rbx), %rax
	setl	%cl
	testq	%rax, %rax
	jne	.L105
	movq	%rbx, %r8
	testb	%cl, %cl
	jne	.L87
.L90:
	cmpq	%rdi, %rdx
	jge	.L69
.L112:
	movq	%r8, %rbx
.L113:
	xorl	%esi, %esi
.L67:
	testq	%rsi, %rsi
	setne	%al
.L94:
	cmpq	%rbx, %r14
	je	.L107
	testb	%al, %al
	je	.L117
.L107:
	movl	$1, %ecx
.L86:
	movq	%rbx, %r8
	movq	%r14, %r9
	movq	%rbp, %rdx
	movq	%rbp, %rbx
	call	_ZSt29_Rb_tree_insert_and_rebalancebPSt18_Rb_tree_node_baseS0_RS_
	addq	$1, 40(%r12)
	jmp	.L111
	.p2align 4,,10
	.p2align 3
.L114:
	cmpq	$0, 40(%r12)
	je	.L60
	movq	32(%r12), %rbx
	cmpq	32(%rbx), %rdi
	jle	.L60
	xorl	%eax, %eax
	jmp	.L94
	.p2align 4,,10
	.p2align 3
.L60:
	movq	16(%r12), %rsi
	testq	%rsi, %rsi
	jne	.L64
	movq	%r13, %rsi
.L62:
	cmpq	%rsi, 24(%r12)
	je	.L118
	movq	%rsi, %rcx
	movq	%rsi, %rbx
	call	_ZSt18_Rb_tree_decrementPSt18_Rb_tree_node_base
	movq	32(%rax), %rdx
	movq	%rax, %rsi
	jmp	.L65
	.p2align 4,,10
	.p2align 3
.L97:
	movq	%rax, %rsi
.L64:
	movq	32(%rsi), %rdx
	movq	24(%rsi), %rax
	cmpq	%rdx, %rdi
	cmovl	16(%rsi), %rax
	setl	%cl
	testq	%rax, %rax
	jne	.L97
	movq	%rsi, %rbx
	testb	%cl, %cl
	jne	.L62
.L65:
	cmpq	%rdx, %rdi
	jg	.L113
	movq	%rsi, %rbx
	jmp	.L69
	.p2align 4,,10
	.p2align 3
.L115:
	cmpq	$0, 24(%rax)
	movq	%r13, %rsi
	jne	.L67
	movq	%rax, %rbx
	xorl	%eax, %eax
	jmp	.L94
	.p2align 4,,10
	.p2align 3
.L117:
	movq	32(%rbx), %rsi
.L85:
	xorl	%ecx, %ecx
	cmpq	%rsi, %rdi
	setl	%cl
	jmp	.L86
	.p2align 4,,10
	.p2align 3
.L83:
	movq	16(%r12), %rbx
	testq	%rbx, %rbx
	jne	.L89
	movq	%r14, %rbx
.L87:
	cmpq	%rbx, 24(%r12)
	je	.L113
	movq	%rbx, %rcx
	call	_ZSt18_Rb_tree_decrementPSt18_Rb_tree_node_base
	movq	%rbx, %r8
	movq	32(%rax), %rdx
	movq	%rax, %rbx
	jmp	.L90
.L116:
	movq	%r14, %rbx
.L75:
	cmpq	%rbx, %rsi
	je	.L113
	movq	%rbx, %rcx
	call	_ZSt18_Rb_tree_decrementPSt18_Rb_tree_node_base
	movq	%rbx, %r8
	movq	32(%rax), %rdx
	movq	%rax, %rbx
	jmp	.L78
	.p2align 4,,10
	.p2align 3
.L118:
	movq	%rsi, %rbx
	xorl	%esi, %esi
	jmp	.L67
	.seh_endproc
	.section .rdata,"dr"
.LC0:
	.ascii "vector::_M_realloc_insert\0"
	.section	.text$_ZNSt6vectorIxSaIxEE17_M_realloc_insertIJRKxEEEvN9__gnu_cxx17__normal_iteratorIPxS1_EEDpOT_,"x"
	.linkonce discard
	.align 2
	.p2align 4
	.globl	_ZNSt6vectorIxSaIxEE17_M_realloc_insertIJRKxEEEvN9__gnu_cxx17__normal_iteratorIPxS1_EEDpOT_
	.def	_ZNSt6vectorIxSaIxEE17_M_realloc_insertIJRKxEEEvN9__gnu_cxx17__normal_iteratorIPxS1_EEDpOT_;	.scl	2;	.type	32;	.endef
	.seh_proc	_ZNSt6vectorIxSaIxEE17_M_realloc_insertIJRKxEEEvN9__gnu_cxx17__normal_iteratorIPxS1_EEDpOT_
_ZNSt6vectorIxSaIxEE17_M_realloc_insertIJRKxEEEvN9__gnu_cxx17__normal_iteratorIPxS1_EEDpOT_:
.LFB11214:
	pushq	%r15
	.seh_pushreg	%r15
	pushq	%r14
	.seh_pushreg	%r14
	pushq	%r13
	.seh_pushreg	%r13
	pushq	%r12
	.seh_pushreg	%r12
	pushq	%rbp
	.seh_pushreg	%rbp
	pushq	%rdi
	.seh_pushreg	%rdi
	pushq	%rsi
	.seh_pushreg	%rsi
	pushq	%rbx
	.seh_pushreg	%rbx
	subq	$56, %rsp
	.seh_stackalloc	56
	.seh_endprologue
	movq	8(%rcx), %rdi
	movq	(%rcx), %rbp
	movq	%rdi, %rax
	subq	%rbp, %rax
	movq	%rdx, %r12
	sarq	$3, %rax
	movq	%rcx, %rsi
	movq	%r8, %r14
	movabsq	$1152921504606846975, %rdx
	cmpq	%rdx, %rax
	je	.L140
	cmpq	%rdi, %rbp
	movl	$1, %edx
	movq	%r12, %r15
	cmovne	%rax, %rdx
	addq	%rdx, %rax
	setc	%dl
	subq	%rbp, %r15
	movzbl	%dl, %edx
	testq	%rdx, %rdx
	jne	.L134
	testq	%rax, %rax
	jne	.L141
	xorl	%ebx, %ebx
	xorl	%r13d, %r13d
.L125:
	movq	(%r14), %rax
	leaq	8(%r13,%r15), %r9
	subq	%r12, %rdi
	leaq	(%r9,%rdi), %r14
	movq	%rax, 0(%r13,%r15)
	testq	%r15, %r15
	jg	.L142
	testq	%rdi, %rdi
	jg	.L130
	testq	%rbp, %rbp
	jne	.L128
.L131:
	movq	%r13, (%rsi)
	movq	%r14, 8(%rsi)
	movq	%rbx, 16(%rsi)
	addq	$56, %rsp
	popq	%rbx
	popq	%rsi
	popq	%rdi
	popq	%rbp
	popq	%r12
	popq	%r13
	popq	%r14
	popq	%r15
	ret
	.p2align 4,,10
	.p2align 3
.L142:
	movq	%r15, %r8
	movq	%rbp, %rdx
	movq	%r13, %rcx
	movq	%r9, 40(%rsp)
	call	memmove
	testq	%rdi, %rdi
	jg	.L143
.L128:
	movq	16(%rsi), %rdx
	movq	%rbp, %rcx
	subq	%rbp, %rdx
	call	_ZdlPvy
	jmp	.L131
	.p2align 4,,10
	.p2align 3
.L130:
	movq	%rdi, %r8
	movq	%r12, %rdx
	movq	%r9, %rcx
	call	memcpy
	testq	%rbp, %rbp
	je	.L131
	jmp	.L128
	.p2align 4,,10
	.p2align 3
.L134:
	movabsq	$9223372036854775800, %rbx
.L124:
	movq	%rbx, %rcx
	call	_Znwy
	movq	%rax, %r13
	addq	%rax, %rbx
	jmp	.L125
	.p2align 4,,10
	.p2align 3
.L143:
	movq	40(%rsp), %rcx
	movq	%r12, %rdx
	movq	%rdi, %r8
	call	memcpy
	movq	16(%rsi), %rdx
	movq	%rbp, %rcx
	subq	%rbp, %rdx
	call	_ZdlPvy
	jmp	.L131
	.p2align 4,,10
	.p2align 3
.L141:
	movabsq	$1152921504606846975, %rdx
	cmpq	%rdx, %rax
	cmova	%rdx, %rax
	leaq	0(,%rax,8), %rbx
	jmp	.L124
.L140:
	leaq	.LC0(%rip), %rcx
	call	_ZSt20__throw_length_errorPKc
	nop
	.seh_endproc
	.def	__main;	.scl	2;	.type	32;	.endef
	.section .rdata,"dr"
.LC1:
	.ascii " \0"
	.section	.text.unlikely,"x"
.LCOLDB2:
	.section	.text.startup,"x"
.LHOTB2:
	.p2align 4
	.globl	main
	.def	main;	.scl	2;	.type	32;	.endef
	.seh_proc	main
main:
.LFB9969:
	pushq	%r15
	.seh_pushreg	%r15
	pushq	%r14
	.seh_pushreg	%r14
	pushq	%r13
	.seh_pushreg	%r13
	pushq	%r12
	.seh_pushreg	%r12
	pushq	%rbp
	.seh_pushreg	%rbp
	pushq	%rdi
	.seh_pushreg	%rdi
	pushq	%rsi
	.seh_pushreg	%rsi
	pushq	%rbx
	.seh_pushreg	%rbx
	subq	$152, %rsp
	.seh_stackalloc	152
	.seh_endprologue
	xorl	%ebp, %ebp
	xorl	%ebx, %ebx
	call	__main
	leaq	32(%rsp), %rdx
	leaq	104(%rsp), %rsi
	movq	.refptr._ZSt3cin(%rip), %r12
	leaq	40(%rsp), %rdi
	leaq	64(%rsp), %r13
	movq	%r12, %rcx
.LEHB0:
	call	_ZNSirsERi
	leaq	36(%rsp), %rdx
	movq	%rax, %rcx
	call	_ZNSirsERi
.LEHE0:
	movl	32(%rsp), %eax
	pxor	%xmm0, %xmm0
	movl	$0, 104(%rsp)
	movq	$0, 112(%rsp)
	movq	%rsi, 120(%rsp)
	movq	%rsi, 128(%rsp)
	movq	$0, 136(%rsp)
	movq	$0, 80(%rsp)
	movq	$0, 40(%rsp)
	movaps	%xmm0, 64(%rsp)
	testl	%eax, %eax
	jle	.L146
	.p2align 4,,10
	.p2align 3
.L145:
	movq	%rdi, %rdx
	movq	%r12, %rcx
.LEHB1:
	call	_ZNSi10_M_extractIxEERSiRT_
	movq	72(%rsp), %rax
	cmpq	%rbp, %rax
	je	.L147
	movq	40(%rsp), %rdx
	addq	$8, %rax
	movq	%rdx, -8(%rax)
	movq	112(%rsp), %rdx
	movq	%rax, 72(%rsp)
	testq	%rdx, %rdx
	je	.L172
.L201:
	movq	40(%rsp), %r8
	movq	%rsi, %r9
	.p2align 4,,10
	.p2align 3
.L153:
	movq	16(%rdx), %rcx
	movq	24(%rdx), %rax
	cmpq	32(%rdx), %r8
	jle	.L150
.L197:
	testq	%rax, %rax
	je	.L196
	movq	%rax, %rdx
	movq	16(%rdx), %rcx
	movq	24(%rdx), %rax
	cmpq	32(%rdx), %r8
	jg	.L197
.L150:
	testq	%rcx, %rcx
	je	.L152
	movq	%rdx, %r9
	movq	%rcx, %rdx
	jmp	.L153
	.p2align 4,,10
	.p2align 3
.L196:
	movq	%r9, %rdx
.L152:
	cmpq	%rsi, %rdx
	je	.L149
	cmpq	32(%rdx), %r8
	jge	.L154
.L149:
	leaq	96(%rsp), %rcx
	leaq	48(%rsp), %r8
	movq	%rdi, 48(%rsp)
	call	_ZNSt8_Rb_treeIxSt4pairIKxiESt10_Select1stIS2_ESt4lessIxESaIS2_EE22_M_emplace_hint_uniqueIJRKSt21piecewise_construct_tSt5tupleIJRS1_EESD_IJEEEEESt17_Rb_tree_iteratorIS2_ESt23_Rb_tree_const_iteratorIS2_EDpOT_.isra.0
	movq	%rax, %rdx
.L154:
	movl	36(%rsp), %r8d
	addl	$1, 40(%rdx)
	cmpl	%ebx, %r8d
	jle	.L198
	addl	$1, %ebx
	cmpl	%r8d, %ebx
	jge	.L162
.L164:
	cmpl	32(%rsp), %ebx
	jl	.L145
	movq	64(%rsp), %rcx
	testq	%rcx, %rcx
	je	.L146
	movq	%rbp, %rdx
	subq	%rcx, %rdx
	call	_ZdlPvy
.L146:
	movq	112(%rsp), %rcx
	call	_ZNSt8_Rb_treeIxSt4pairIKxiESt10_Select1stIS2_ESt4lessIxESaIS2_EE8_M_eraseEPSt13_Rb_tree_nodeIS2_E.isra.0
	xorl	%eax, %eax
	addq	$152, %rsp
	popq	%rbx
	popq	%rsi
	popq	%rdi
	popq	%rbp
	popq	%r12
	popq	%r13
	popq	%r14
	popq	%r15
	ret
	.p2align 4,,10
	.p2align 3
.L198:
	movl	%ebx, %eax
	movq	64(%rsp), %rdx
	subl	%r8d, %eax
	cltq
	leaq	(%rdx,%rax,8), %r11
	movq	112(%rsp), %rdx
	testq	%rdx, %rdx
	je	.L175
	movq	(%r11), %r9
	movq	%rsi, %r10
	.p2align 4,,10
	.p2align 3
.L160:
	movq	16(%rdx), %rcx
	movq	24(%rdx), %rax
	cmpq	32(%rdx), %r9
	jle	.L157
.L200:
	testq	%rax, %rax
	je	.L199
	movq	%rax, %rdx
	movq	16(%rdx), %rcx
	movq	24(%rdx), %rax
	cmpq	32(%rdx), %r9
	jg	.L200
.L157:
	testq	%rcx, %rcx
	je	.L159
	movq	%rdx, %r10
	movq	%rcx, %rdx
	jmp	.L160
	.p2align 4,,10
	.p2align 3
.L199:
	movq	%r10, %rdx
.L159:
	cmpq	%rsi, %rdx
	je	.L156
	cmpq	32(%rdx), %r9
	jge	.L161
.L156:
	leaq	96(%rsp), %rcx
	leaq	56(%rsp), %r8
	movq	%r11, 56(%rsp)
	call	_ZNSt8_Rb_treeIxSt4pairIKxiESt10_Select1stIS2_ESt4lessIxESaIS2_EE22_M_emplace_hint_uniqueIJRKSt21piecewise_construct_tSt5tupleIJRS1_EESD_IJEEEEESt17_Rb_tree_iteratorIS2_ESt23_Rb_tree_const_iteratorIS2_EDpOT_.isra.0
	movl	36(%rsp), %r8d
	movq	%rax, %rdx
.L161:
	addl	$1, %ebx
	subl	$1, 40(%rdx)
	cmpl	%r8d, %ebx
	jl	.L164
.L162:
	movq	120(%rsp), %rcx
	cmpq	%rsi, %rcx
	je	.L164
	addl	$1, %r8d
	movl	40(%rcx), %r14d
	movq	32(%rcx), %rax
	movl	%r8d, %r15d
	shrl	$31, %r15d
	addl	%r8d, %r15d
	sarl	%r15d
	cmpl	%r14d, %r15d
	jle	.L165
	.p2align 4,,10
	.p2align 3
.L166:
	call	_ZSt18_Rb_tree_incrementPSt18_Rb_tree_node_base
	movq	%rax, %rcx
	cmpq	%rsi, %rax
	je	.L164
	addl	40(%rcx), %r14d
	cmpl	%r14d, %r15d
	jg	.L166
	movq	32(%rcx), %rax
.L165:
	movq	.refptr._ZSt4cout(%rip), %rcx
	movq	%rax, %rdx
	call	_ZNSo9_M_insertIxEERSoT_
	movq	%rax, %rcx
	movl	$1, %r8d
	leaq	.LC1(%rip), %rdx
	call	_ZSt16__ostream_insertIcSt11char_traitsIcEERSt13basic_ostreamIT_T0_ES6_PKS3_x
	jmp	.L164
	.p2align 4,,10
	.p2align 3
.L147:
	movq	%rdi, %r8
	movq	%rbp, %rdx
	movq	%r13, %rcx
	call	_ZNSt6vectorIxSaIxEE17_M_realloc_insertIJRKxEEEvN9__gnu_cxx17__normal_iteratorIPxS1_EEDpOT_
.LEHE1:
	movq	112(%rsp), %rdx
	movq	80(%rsp), %rbp
	testq	%rdx, %rdx
	jne	.L201
	.p2align 4,,10
	.p2align 3
.L172:
	movq	%rsi, %rdx
	jmp	.L149
.L175:
	movq	%rsi, %rdx
	jmp	.L156
.L178:
	movq	%rax, %rbx
	jmp	.L169
	.def	__gxx_personality_seh0;	.scl	2;	.type	32;	.endef
	.seh_handler	__gxx_personality_seh0, @unwind, @except
	.seh_handlerdata
.LLSDA9969:
	.byte	0xff
	.byte	0xff
	.byte	0x1
	.uleb128 .LLSDACSE9969-.LLSDACSB9969
.LLSDACSB9969:
	.uleb128 .LEHB0-.LFB9969
	.uleb128 .LEHE0-.LEHB0
	.uleb128 0
	.uleb128 0
	.uleb128 .LEHB1-.LFB9969
	.uleb128 .LEHE1-.LEHB1
	.uleb128 .L178-.LFB9969
	.uleb128 0
.LLSDACSE9969:
	.section	.text.startup,"x"
	.seh_endproc
	.section	.text.unlikely,"x"
	.def	main.cold;	.scl	3;	.type	32;	.endef
	.seh_proc	main.cold
	.seh_stackalloc	216
	.seh_savereg	%rbx, 152
	.seh_savereg	%rsi, 160
	.seh_savereg	%rdi, 168
	.seh_savereg	%rbp, 176
	.seh_savereg	%r12, 184
	.seh_savereg	%r13, 192
	.seh_savereg	%r14, 200
	.seh_savereg	%r15, 208
	.seh_endprologue
main.cold:
.L169:
	movq	64(%rsp), %rcx
	movq	80(%rsp), %rdx
	subq	%rcx, %rdx
	testq	%rcx, %rcx
	je	.L170
	call	_ZdlPvy
.L170:
	movq	112(%rsp), %rcx
	call	_ZNSt8_Rb_treeIxSt4pairIKxiESt10_Select1stIS2_ESt4lessIxESaIS2_EE8_M_eraseEPSt13_Rb_tree_nodeIS2_E.isra.0
	movq	%rbx, %rcx
.LEHB2:
	call	_Unwind_Resume
	nop
.LEHE2:
	.seh_handler	__gxx_personality_seh0, @unwind, @except
	.seh_handlerdata
.LLSDAC9969:
	.byte	0xff
	.byte	0xff
	.byte	0x1
	.uleb128 .LLSDACSEC9969-.LLSDACSBC9969
.LLSDACSBC9969:
	.uleb128 .LEHB2-.LCOLDB2
	.uleb128 .LEHE2-.LEHB2
	.uleb128 0
	.uleb128 0
.LLSDACSEC9969:
	.section	.text.unlikely,"x"
	.section	.text.startup,"x"
	.section	.text.unlikely,"x"
	.seh_endproc
.LCOLDE2:
	.section	.text.startup,"x"
.LHOTE2:
	.p2align 4
	.def	_GLOBAL__sub_I_main;	.scl	3;	.type	32;	.endef
	.seh_proc	_GLOBAL__sub_I_main
_GLOBAL__sub_I_main:
.LFB12013:
	subq	$40, %rsp
	.seh_stackalloc	40
	.seh_endprologue
	leaq	_ZStL8__ioinit(%rip), %rcx
	call	_ZNSt8ios_base4InitC1Ev
	leaq	__tcf_0(%rip), %rcx
	addq	$40, %rsp
	jmp	atexit
	.seh_endproc
	.section	.ctors,"w"
	.align 8
	.quad	_GLOBAL__sub_I_main
.lcomm _ZStL8__ioinit,1,1
	.ident	"GCC: (MinGW-W64 x86_64-ucrt-posix-seh, built by Brecht Sanders) 12.2.0"
	.def	_ZNSt8ios_base4InitD1Ev;	.scl	2;	.type	32;	.endef
	.def	_ZdlPvy;	.scl	2;	.type	32;	.endef
	.def	_Znwy;	.scl	2;	.type	32;	.endef
	.def	_ZSt18_Rb_tree_decrementPSt18_Rb_tree_node_base;	.scl	2;	.type	32;	.endef
	.def	_ZSt18_Rb_tree_incrementPSt18_Rb_tree_node_base;	.scl	2;	.type	32;	.endef
	.def	_ZSt29_Rb_tree_insert_and_rebalancebPSt18_Rb_tree_node_baseS0_RS_;	.scl	2;	.type	32;	.endef
	.def	memmove;	.scl	2;	.type	32;	.endef
	.def	memcpy;	.scl	2;	.type	32;	.endef
	.def	_ZSt20__throw_length_errorPKc;	.scl	2;	.type	32;	.endef
	.def	_ZNSirsERi;	.scl	2;	.type	32;	.endef
	.def	_ZNSi10_M_extractIxEERSiRT_;	.scl	2;	.type	32;	.endef
	.def	_ZNSo9_M_insertIxEERSoT_;	.scl	2;	.type	32;	.endef
	.def	_ZSt16__ostream_insertIcSt11char_traitsIcEERSt13basic_ostreamIT_T0_ES6_PKS3_x;	.scl	2;	.type	32;	.endef
	.def	_Unwind_Resume;	.scl	2;	.type	32;	.endef
	.def	_ZNSt8ios_base4InitC1Ev;	.scl	2;	.type	32;	.endef
	.def	atexit;	.scl	2;	.type	32;	.endef
	.section	.rdata$.refptr._ZSt4cout, "dr"
	.globl	.refptr._ZSt4cout
	.linkonce	discard
.refptr._ZSt4cout:
	.quad	_ZSt4cout
	.section	.rdata$.refptr._ZSt3cin, "dr"
	.globl	.refptr._ZSt3cin
	.linkonce	discard
.refptr._ZSt3cin:
	.quad	_ZSt3cin
